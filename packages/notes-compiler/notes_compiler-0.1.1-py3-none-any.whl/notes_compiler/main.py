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


class Config:
    def __init__(self, config: Dict):
        self.config = config

    @staticmethod
    def from_json(filename: str):
        logging.info(f"Loading configuration from JSON file: {filename}")
        with open(filename, "r") as file:
            return Config(json.loads(file.read()))

    @staticmethod
    def default():
        return Config({"css": ["custom_style.css"]})


class MarkdownTreeProcessor:
    def __init__(self, root_path: str, output_path: str, global_config: Config):
        self.root_path = root_path
        self.output_path = output_path
        self.global_config = global_config
        self._process()

    def _process(self):
        self.md_tree = self._get_md_tree(self.root_path)
        self.copy_tree = self._get_copy_tree(self.root_path)
        self.html_tree = self._process_md_tree(self.md_tree, [])

    def output(self):
        self._sync_directories(self.html_tree, self.output_path, [])
        self._write_html_tree(self.html_tree, self.output_path, [])
        self._write_copy_tree(self.copy_tree, self.output_path, [])

    def _get_md_tree(self, root_path: str) -> Dict:
        md_tree = dict()
        for entry in os.scandir(root_path):
            stem = Path(entry.path).stem
            if entry.is_dir():
                md_tree[stem] = self._get_md_tree(entry.path)
            elif entry.is_file() and entry.name.endswith(".md"):
                with open(entry.path, "r") as file:
                    md_tree[stem] = file.read()
        return md_tree

    def _get_copy_tree(self, root_path: str) -> Dict:
        copy_tree = dict()
        for entry in os.scandir(root_path):
            stem = Path(entry.path).stem
            if entry.is_dir():
                copy_tree[stem] = self._get_copy_tree(entry.path)
            elif entry.is_file() and not entry.name.endswith(".md"):
                copy_tree[stem] = (entry.path, entry.name)
        return copy_tree

    def _sync_directories(self, tree: Dict, output_path: str, prefix: List[str]):
        full_path = f"{output_path}/{self._get_path_from_prefix(prefix)}"
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        for name, item in tree.items():
            if isinstance(item, dict):
                self._sync_directories(
                    tree=item, output_path=output_path, prefix=prefix + [name]
                )

    def _process_md_tree(self, md_tree: Dict, prefix: List[str]) -> Dict:
        html_tree = dict()
        if len(prefix) == 0:
            html_tree["index"] = self._make_html_file(
                body=self._toc(md_tree, []), name="table_of_contents", prefix=[]
            )
        for name, item in md_tree.items():
            if isinstance(item, dict):
                html_tree[name] = self._process_md_tree(item, prefix + [name])
            elif isinstance(item, str):
                html_tree[name] = self._make_html_file(
                    body=self._compile_markdown(item), name=name, prefix=prefix
                )
        return html_tree

    def _write_html_tree(self, html_tree: Dict, output_path: str, prefix: List[str]):
        for name, item in html_tree.items():
            if isinstance(item, dict):
                html_tree[name] = self._write_html_tree(
                    item, output_path, prefix + [name]
                )
            elif isinstance(item, str):
                with open(
                    f"{output_path}/{self._get_path_from_prefix(prefix)}/{name}.html",
                    "w",
                ) as f:
                    f.write(item)

    def _write_copy_tree(self, copy_tree: Dict, output_path: str, prefix: List[str]):
        for name, item in copy_tree.items():
            if isinstance(item, dict):
                self._write_copy_tree(
                    copy_tree=item, output_path=output_path, prefix=prefix + [name]
                )
            elif isinstance(item, Tuple):
                path, name = item
                shutil.copyfile(
                    path, f"{output_path}/{self._get_path_from_prefix(prefix)}/{name}"
                )

    def _get_path_from_prefix(self, prefix: List[str]):
        if len(prefix) == 0:
            return ""
        return reduce(lambda a, b: f"{a}/{b}", prefix)

    def _compile_markdown(self, md: str) -> str:
        return markdown.markdown(md, tab_length=2, extensions=[KatexExtension()])

    def _make_html_file(
        self,
        body: str,
        name: str,
        prefix: List[str],
    ) -> str:
        html = HtmlPage()
        html.body = body
        html.name = name
        html.prefix = prefix
        if "css" in self.global_config.config:
            for css in self.global_config.config["css"]:
                html.css.append(css)
        return html.build_page()

    def _toc(self, tree: Dict, prefix: List[str]) -> str:
        def make_toc(compiled: Dict, prefix: List[str]) -> str:
            if len(prefix) == 0:
                toc_str = ""
            else:
                toc_str = "<ul>\n"
            for name, item in compiled.items():
                if isinstance(item, dict):
                    if len(prefix) == 0:
                        toc_str += f"<h2>{snake_case_to_title_case(name)}</h2>\n{make_toc(item, prefix=prefix + [name])}"
                    else:
                        toc_str += f"<li>{snake_case_to_title_case(name)}\n{make_toc(item, prefix=prefix + [name])}</li>"
                elif isinstance(item, str):
                    toc_str += f'<li><a href="{self._get_path_from_prefix(prefix)}/{name}.html">{snake_case_to_title_case(name)}</a></li>\n'
            if len(prefix) == 0:
                toc_str += ""
            else:
                toc_str += "</ul>"
            return toc_str

        toc_str = "<h1>Table of Contents</h1>\n" + make_toc(tree, prefix)

        return toc_str


class HtmlPage:
    def __init__(self):
        self.body = ""
        self.css = []
        self.name: Optional[str] = None
        self.prefix = []

    def build_page(self) -> str:
        return f"""
<html>
    <head>
        {reduce(lambda a,b: f'{a} {b}', (self.get_css_link(css) for css in self.css), '')}
    </head>

    <body>
        {self.body}
    </body>
</html>
"""

    def get_css_link(self, css: str) -> str:
        if len(self.prefix) == 0:
            css_path = css
        else:
            css_path = (
                reduce(lambda a, b: f"{a}/{b}", [".." for _ in self.prefix]) + f"/{css}"
            )
        return f'<link rel="stylesheet" href="{css_path}"/>'


def main():
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


def snake_case_to_title_case(snake_case: str) -> str:
    return snake_case.replace("_", " ").capitalize()
