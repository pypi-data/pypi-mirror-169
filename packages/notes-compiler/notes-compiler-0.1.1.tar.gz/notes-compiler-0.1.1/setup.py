# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notes_compiler']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.4.1,<4.0.0', 'markdown-katex>=202112.1034,<202113.0']

entry_points = \
{'console_scripts': ['notes = notes_compiler.main:main']}

setup_kwargs = {
    'name': 'notes-compiler',
    'version': '0.1.1',
    'description': '',
    'long_description': '# notes-compiler\n\n## Usage\n\n```bash\nnotes <input_path> <output_path>\n```\n\nFor example:\n\n```bash\nnotes ./src ./public\n```\n\n## Installation\n\nWhile on the root of this repository:\n\n```bash\npoetry install\npoetry build\ncd dist\npip install notes_compiler-<VERSION>-py3-none-any.whl --force-reinstal\n```\n\nreplacing `<VERSION` with the actual version number.\n',
    'author': 'Manuel Brea',
    'author_email': 'm.brea.carreras@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
