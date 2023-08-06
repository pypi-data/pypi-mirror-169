import argparse
from typing import Dict, List, Optional, Self
from pathlib import Path
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from functools import reduce
from markdown_katex import KatexExtension
import os
import os.path
import shutil
import json
import logging
import importlib.resources
from dataclasses import dataclass, field


class Config:
    def __init__(self, config: Dict):
        self.config = config

    @classmethod
    def from_json(cls, json_text: str) -> Self:
        return cls.default().merge_with(cls(json.loads(json_text)))

    @classmethod
    def from_json_file(cls, filename: str) -> Self:
        with open(filename, "r") as file:
            return cls.default().merge_with(cls(json.loads(file.read())))

    @classmethod
    def default(cls) -> Self:
        raise NotImplementedError()

    def merge_with(self, other: Self) -> Self:
        def merge_configs(source, destination):
            for key, value in source.items():
                if isinstance(value, dict):
                    node = destination.setdefault(key, {})
                    merge_configs(value, node)
                elif (
                    isinstance(value, list)
                    and key in destination
                    and isinstance(destination[key], list)
                ):
                    destination[key].extend(value)
                else:
                    destination[key] = value

            return destination

        self.config = merge_configs(other.config, self.config)
        return self

    def __getattr__(self, name):
        if name in self.config:
            return self.config[name]
        else:
            raise AttributeError(name)


class ProjectConfig(Config):
    @classmethod
    def default(cls) -> Self:
        return cls(
            {
                "css": ["header.css", "custom_style.css"],
                "root": ".",
                "src_root": "src",
                "public_root": "public",
            }
        )

    @classmethod
    def from_json_file(cls, filename: str) -> Self:
        root = os.path.dirname(os.path.abspath(filename))
        return super().from_json_file(filename).merge_with(cls({"root": root}))


class FolderConfig(Config):
    @classmethod
    def default(cls) -> Self:
        return cls({"build_index": False})


class HtmlPage:
    def __init__(
        self,
        parent: "MarkdownTreeNode",
        body: str = "",
        css: Optional[List[str]] = None,
        name: str = "",
    ):
        self.parent = parent
        self.body: str = body
        self.css: List[str] = css.copy() if css else []
        self.name: str = name
        self.prefix: List[str] = []
        self.page_before: Optional[HtmlPage] = None
        self.page_after: Optional[HtmlPage] = None

    @staticmethod
    def from_markdown(md: str, **kwargs):
        html = HtmlPage._compile_markdown(md)
        return HtmlPage(body=html, **kwargs)

    @staticmethod
    def _compile_markdown(md: str) -> str:
        return markdown.markdown(
            md,
            tab_length=2,
            extensions=[
                CodeHiliteExtension(),
                KatexExtension(),
                "python3_markdown_extension_graphviz",
            ],
        )

    def build_page(self) -> str:
        return f"""
<html>
    <head>
        {reduce(lambda a,b: f'{a} {b}', (self.get_css_link(css) for css in self.css), '')}
    </head>

    <body>
        <header>
        {self._get_header()}
        </header>
        {self.body}
        <footer>
        {self._get_header()}
        </footer>
    </body>
</html>
"""

    def _get_link_to_page(self, page: "HtmlPage") -> str:
        return f"{self.parent.path_to_root()}/{page.parent.path_from_root()}/{page.name}.html"

    def _get_header(self):
        node = self.parent
        linked_index = None
        if self.name == "index":
            node = node.parent
        while node is not None and linked_index is None:
            linked_index = node.content["index"]
            node = node.parent
        return f"""
            {f'<a class="link-before" href={self._get_link_to_page(self.page_before)}><small>&#9664; {snake_case_to_title_case(self.page_before.name)}</small></a>' if self.page_before else '<div class="link-before"></div>'}
            {f'<a class="link-index" href={self._get_link_to_page(linked_index["page"])}><small>To Index</small></a>' if linked_index else '<div class="link-index"></div>'}
            {f'<a class="link-after" href={self._get_link_to_page(self.page_after)}><small>{snake_case_to_title_case(self.page_after.name)} &#9654;</small></a>' if self.page_after else '<div class="link-after"></div>'}
"""

    def get_css_link(self, css: str) -> str:
        return f'<link rel="stylesheet" href="{self.parent.path_to_root()}/{css}"/>'


@dataclass
class MarkdownTreeNode:
    name: str
    parent: Optional["MarkdownTreeNode"] = None
    children: List["MarkdownTreeNode"] = field(default_factory=list)
    content: Dict = field(default_factory=dict)
    folder_config: FolderConfig = field(default_factory=FolderConfig.default)

    def path_from_root(self):
        if self.parent is None:
            return "."
        else:
            return f"{self.parent.path_from_root()}/{self.name}"

    def path_to_root(self):
        if self.parent is None:
            return "."
        else:
            return f"../{self.parent.path_to_root()}"

    def _print_with_depth(self, d: int = 0) -> str:
        str_repr = f"{'├──' if d else ''}{'───' * max(d - 1, 0)}{self.name}\n"
        for child in self.children:
            str_repr += child._print_with_depth(d + 1)
        str_repr += "|  " * d + "└──────\n"
        return str_repr

    def __str__(self) -> str:
        return self._print_with_depth(0)


class MarkdownTreeProcessor:
    def __init__(self, project_config: ProjectConfig):
        self.project_config = project_config
        self.src_root = (
            project_config.src_root
            if os.path.isabs(project_config.src_root)
            else f"{project_config.root}/{project_config.src_root}"
        )
        self.public_root = (
            project_config.public_root
            if os.path.isabs(project_config.public_root)
            else f"{project_config.root}/{project_config.public_root}"
        )
        self._process()

    def _process(self):
        logging.info("Reading tree...")
        self.tree = self._read_tree(self.src_root)
        logging.info("Reading markdown files...")
        self._read_markdown(self.tree)
        logging.info("Finding files to copy...")
        self._read_files_to_copy(self.tree)
        logging.info("Building HTML pages...")
        self._make_pages(self.tree)
        logging.info("Processing links...")
        self._decorate_pages(self.tree)

    def output(self):
        self._sync_directories(self.tree)
        self._write_html_tree(self.tree)
        self._write_copy_tree(self.tree)

    def _read_tree(
        self, root_path: str, parent: Optional[MarkdownTreeNode] = None, name: str = ""
    ) -> MarkdownTreeNode:
        config_path = f"{root_path}/notes-folderrc.json"
        if os.path.isfile(config_path):
            config = FolderConfig.from_json_file(config_path)
        else:
            config = FolderConfig.default()
        tree = MarkdownTreeNode(name=name, parent=parent, folder_config=config)
        for entry in os.scandir(root_path):
            if entry.is_dir():
                tree.children.append(
                    self._read_tree(entry.path, name=entry.name, parent=tree)
                )
        return tree

    def _read_markdown(self, tree: MarkdownTreeNode):
        """
        . -> md
        """
        tree.content["markdown"] = []
        for entry in os.scandir(f"{self.src_root}/{tree.path_from_root()}"):
            if entry.is_file() and entry.name.endswith(".md"):
                stem = Path(entry.path).stem
                with open(entry.path, "r") as file:
                    tree.content["markdown"].append(
                        {
                            "name": stem,
                            "content": file.read(),
                            "filename": entry.name,
                        }
                    )
        for child in tree.children:
            self._read_markdown(child)

    def _read_files_to_copy(self, tree: MarkdownTreeNode):
        """
        . -> pages
        """
        tree.content["copy"] = []

        # Builtin files
        if tree.parent is None:
            for traversable in importlib.resources.files(
                "notes_compiler.resources"
            ).iterdir():
                if str(traversable).endswith(".css"):
                    with importlib.resources.as_file(traversable) as path:
                        tree.content["copy"].append(
                            {"path": path, "filename": os.path.basename(path)}
                        )

        # User-created files
        for entry in os.scandir(f"{self.src_root}/{tree.path_from_root()}"):
            if entry.is_file() and not entry.name.endswith(".md"):
                tree.content["copy"].append(
                    {"path": entry.path, "filename": entry.name}
                )
        for child in tree.children:
            self._read_files_to_copy(child)

    def _make_pages(self, tree: MarkdownTreeNode):
        """
        md -> pages
        """
        logging.info(f"Building pages at {tree.path_from_root()}")
        tree.content["pages"] = []
        for md in tree.content["markdown"]:
            tree.content["pages"].append(
                {
                    "name": md["name"],
                    "md_filename": md["filename"],
                    "html_filename": md["name"] + ".html",
                    "page": HtmlPage.from_markdown(
                        md=md["content"],
                        name=md["name"],
                        css=self.project_config.css,
                        parent=tree,
                    ),
                }
            )
        key = lambda page: page["name"]
        tree.content["pages"] = sorted(tree.content["pages"], key=key)
        for child in tree.children:
            self._make_pages(child)

    def _decorate_pages(self, tree: MarkdownTreeNode):
        """
        pages -> pages
        """
        if tree.folder_config.build_index:
            tree.content["index"] = {
                "name": "index",
                "html_filename": "index.html",
                "page": HtmlPage(
                    body=self._toc(tree),
                    name="index",
                    css=self.project_config.css,
                    parent=tree,
                ),
            }
        else:
            tree.content["index"] = None
        for i, page in enumerate(tree.content["pages"]):
            if i > 0:
                page["page"].page_before = tree.content["pages"][i - 1]["page"]
            if i < len(tree.content["pages"]) - 1:
                page["page"].page_after = tree.content["pages"][i + 1]["page"]
        for child in tree.children:
            self._decorate_pages(child)

    def _sync_directories(self, tree: MarkdownTreeNode):
        full_path = f"{self.public_root}/{tree.path_from_root()}"
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        for child in tree.children:
            self._sync_directories(child)

    def _write_html_tree(self, tree: MarkdownTreeNode):
        """
        pages -> .
        """
        for child in tree.children:
            self._write_html_tree(child)

        if tree.folder_config.build_index:
            with open(
                f"{self.public_root}/{tree.path_from_root()}/{tree.content['index']['html_filename']}",
                "w",
            ) as f:
                f.write(tree.content["index"]["page"].build_page())
        for page in tree.content["pages"]:
            with open(
                f"{self.public_root}/{tree.path_from_root()}/{page['html_filename']}",
                "w",
            ) as f:
                f.write(page["page"].build_page())

    def _write_copy_tree(self, tree: MarkdownTreeNode):
        """
        copy -> .
        """
        for child in tree.children:
            self._write_copy_tree(child)
        for copy in tree.content["copy"]:
            shutil.copyfile(
                copy["path"],
                f"{self.public_root}/{tree.path_from_root()}/{copy['filename']}",
            )

    def _toc(self, tree: MarkdownTreeNode) -> str:
        """
        pages -> .
        """

        def make_toc(tree: MarkdownTreeNode, root: MarkdownTreeNode) -> str:
            toc_str = "<ul>\n"
            for child in tree.children:
                if child.folder_config.build_index:
                    path_to_index = (
                        f"{tree.path_to_root()}/{child.path_from_root()}/index.html"
                    )
                    toc_str += f'<li><a href="{path_to_index}">🗁 {snake_case_to_title_case(child.name)}</a>\n{make_toc(child, root)}</li>'
                else:
                    toc_str += f"<li>🗁 {snake_case_to_title_case(child.name)}\n{make_toc(child, root)}</li>"
            for page in tree.content["pages"]:
                toc_str += f'<li><a href="{root.path_to_root()}/{tree.path_from_root()}/{page["html_filename"]}">{snake_case_to_title_case(page["name"])}</a></li>\n'
            toc_str += "</ul>"
            return toc_str

        toc_str = (
            f"<h1>{snake_case_to_title_case(tree.name) if tree.name else 'Table of Contents'}</h1>\n"
            + make_toc(tree, tree)
        )

        return toc_str


def main():
    setup_logging()
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, default=".")
    args = parser.parse_args()

    json_config_path = find_file_upwards("notes-projectrc.json", args.path)
    if json_config_path is not None:
        logging.info(f"Loading configuration from JSON file: {json_config_path}")
        config = ProjectConfig.from_json_file(json_config_path)
    else:
        raise Exception(
            "No notes-projectrc.json file found in target directory nor any of its parents."
        )

    tree_processor = MarkdownTreeProcessor(project_config=config)
    tree_processor.output()


def snake_case_to_title_case(snake_case: str) -> str:
    return snake_case.replace("_", " ").capitalize()


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        style="{",
        format="[{levelname}({name}):{filename}:{funcName}] {message}",
    )


def find_file_upwards(filename: str, dir: str = ".") -> Optional[str]:
    dir = os.path.abspath(dir)
    for entry in os.scandir(dir):
        if entry.is_file() and entry.name == filename:
            return entry.path
    if dir == "/":
        return None
    parent_dir = os.path.dirname(dir)
    return find_file_upwards(filename, parent_dir)
