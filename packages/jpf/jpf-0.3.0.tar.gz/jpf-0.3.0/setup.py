# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jpf']

package_data = \
{'': ['*']}

install_requires = \
['plac>=1.3.5,<2.0.0']

entry_points = \
{'console_scripts': ['jpf = jpf:main']}

setup_kwargs = {
    'name': 'jpf',
    'version': '0.3.0',
    'description': 'Pretty format all your json files at once in place with three characters',
    'long_description': '# jpf\n\n[![Conda Recipe](https://img.shields.io/badge/recipe-jpf-green.svg)](https://anaconda.org/conda-forge/jpf)\n[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/jpf.svg)](https://anaconda.org/conda-forge/jpf)\n[![Conda Version](https://img.shields.io/conda/vn/conda-forge/jpf.svg)](https://anaconda.org/conda-forge/jpf)\n![License](https://img.shields.io/github/license/fxwiegand/jpf)\n![PyPI](https://img.shields.io/pypi/v/jpf)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/jpf)\n\n\nPretty format all your json files at once in place with three characters\n\n## Usage\n\n```jpf```\n\nJust typing in the three magic characters will pretty format all your `*.json` files in the current folder and all subfolders.\nSince the command is recursive `jpf` should be used with caution.\n\n## Options\n\n`jpf` comes with some options to further customise the formatting of your files:\n\n| argument      | short | default | function                                |\n|---------------|-------|---------|-----------------------------------------|\n| `--help`      | `-h`  |         | show this help message and exit         |\n| `--indent`    | `-i`  | 4       | format files with that indent level     |\n| `--sort-keys` | `-s`  | False   | decide whether jpf should sort the keys |\n\n## Installation\n\n### pip\n\n`jpf` is as very simple to install using pip:\n\n```pip install jpf```\n\n### conda\n\nAlternatively `jpf` can be installed using conda:\n\n```conda install -c conda-forge jpf```\n',
    'author': 'fxwiegand',
    'author_email': 'fxwiegand@wgdnet.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fxwiegand/jpf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
