import argparse
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import markdown
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

    @staticmethod
    def from_json(filename: str):
        logging.info(f"Loading configuration from JSON file: {filename}")
        with open(filename, "r") as file:
            return Config.builtin().merge_with(Config(json.loads(file.read())))

    @staticmethod
    def default():
        return Config.builtin().merge_with(Config({"css": ["custom_style.css"]}))

    @staticmethod
    def builtin():
        return Config({"css": ["header.css"]})

    def merge_with(self, other: "Config"):
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
            extensions=[KatexExtension(), "python3_markdown_extension_graphviz"],
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
        if self.name != "index":
            linked_index = self.parent.content["index"]["page"]
        elif self.parent.parent != None:
            linked_index = self.parent.parent.content["index"]["page"]
        else:
            linked_index = None
        return f"""
            {f'<a class="link-before" href={self._get_link_to_page(self.page_before)}><small>&#9664; {snake_case_to_title_case(self.page_before.name)}</small></a>' if self.page_before else '<div class="link-before"></div>'}
            {f'<a class="link-index" href={self._get_link_to_page(linked_index)}><small>To Index</small></a>' if linked_index else '<div class="link-index"></div>'}
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


class MarkdownTreeProcessor:
    def __init__(self, root_path: str, output_path: str, global_config: Config):
        self.root_path = root_path
        self.output_path = output_path
        self.global_config = global_config
        self._process()

    def _process(self):
        self.tree = self._read_tree(self.root_path)
        self._read_markdown(self.tree)
        self._read_files_to_copy(self.tree)
        self._make_pages(self.tree)
        self._decorate_pages(self.tree)

    def output(self):
        self._sync_directories(self.tree)
        self._write_html_tree(self.tree)
        self._write_copy_tree(self.tree)

    def _read_tree(
        self, root_path: str, parent: Optional[MarkdownTreeNode] = None, name: str = ""
    ) -> MarkdownTreeNode:
        tree = MarkdownTreeNode(name=name, parent=parent)
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
        for entry in os.scandir(f"{self.root_path}/{tree.path_from_root()}"):
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
        for entry in os.scandir(f"{self.root_path}/{tree.path_from_root()}"):
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
                        css=self.global_config.css,
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
        tree.content["index"] = {
            "name": "index",
            "html_filename": "index.html",
            "page": HtmlPage(
                body=self._toc(tree),
                name="index",
                css=self.global_config.css,
                parent=tree,
            ),
        }
        for i, page in enumerate(tree.content["pages"]):
            if i > 0:
                page["page"].page_before = tree.content["pages"][i - 1]["page"]
            if i < len(tree.content["pages"]) - 1:
                page["page"].page_after = tree.content["pages"][i + 1]["page"]
        for child in tree.children:
            self._decorate_pages(child)

    def _sync_directories(self, tree: MarkdownTreeNode):
        full_path = f"{self.output_path}/{tree.path_from_root()}"
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        for child in tree.children:
            self._sync_directories(child)

    def _write_html_tree(self, tree: MarkdownTreeNode):
        """
        pages -> .
        """
        for child in tree.children:
            self._write_html_tree(child)

        with open(
            f"{self.output_path}/{tree.path_from_root()}/{tree.content['index']['html_filename']}",
            "w",
        ) as f:
            f.write(tree.content["index"]["page"].build_page())
        for page in tree.content["pages"]:
            with open(
                f"{self.output_path}/{tree.path_from_root()}/{page['html_filename']}",
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
                f"{self.output_path}/{tree.path_from_root()}/{copy['filename']}",
            )

    def _toc(self, tree: MarkdownTreeNode) -> str:
        """
        pages -> .
        """

        def make_toc(tree: MarkdownTreeNode, root: MarkdownTreeNode) -> str:
            toc_str = "<ul>\n"
            for child in tree.children:
                path_to_index = (
                    f"{tree.path_to_root()}/{child.path_from_root()}/index.html"
                )
                toc_str += f'<li><a href="{path_to_index}">{snake_case_to_title_case(child.name)}</a>\n{make_toc(child, root)}</li>'
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
    parser.add_argument("input_path", type=str, default="./src")
    parser.add_argument("output_path", type=str, default="./public")
    args = parser.parse_args()

    json_config_path = f"{args.input_path}/notes-config.json"
    if os.path.exists(json_config_path) and os.path.isfile(json_config_path):
        config = Config.from_json(json_config_path)
    else:
        config = Config.default()

    tree_processor = MarkdownTreeProcessor(
        args.input_path, args.output_path, global_config=config
    )

    tree_processor.output()

    for traversable in importlib.resources.files("notes_compiler.resources").iterdir():
        if str(traversable).endswith(".css"):
            with importlib.resources.as_file(traversable) as path:
                shutil.copy(path, args.output_path)


def snake_case_to_title_case(snake_case: str) -> str:
    return snake_case.replace("_", " ").capitalize()


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        style="{",
        format="[{levelname}({name}):{filename}:{funcName}] {message}",
    )
