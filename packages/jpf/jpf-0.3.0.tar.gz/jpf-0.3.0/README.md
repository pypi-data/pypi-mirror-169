# jpf

[![Conda Recipe](https://img.shields.io/badge/recipe-jpf-green.svg)](https://anaconda.org/conda-forge/jpf)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/jpf.svg)](https://anaconda.org/conda-forge/jpf)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/jpf.svg)](https://anaconda.org/conda-forge/jpf)
![License](https://img.shields.io/github/license/fxwiegand/jpf)
![PyPI](https://img.shields.io/pypi/v/jpf)
![PyPI - Downloads](https://img.shields.io/pypi/dm/jpf)


Pretty format all your json files at once in place with three characters

## Usage

```jpf```

Just typing in the three magic characters will pretty format all your `*.json` files in the current folder and all subfolders.
Since the command is recursive `jpf` should be used with caution.

## Options

`jpf` comes with some options to further customise the formatting of your files:

| argument      | short | default | function                                |
|---------------|-------|---------|-----------------------------------------|
| `--help`      | `-h`  |         | show this help message and exit         |
| `--indent`    | `-i`  | 4       | format files with that indent level     |
| `--sort-keys` | `-s`  | False   | decide whether jpf should sort the keys |

## Installation

### pip

`jpf` is as very simple to install using pip:

```pip install jpf```

### conda

Alternatively `jpf` can be installed using conda:

```conda install -c conda-forge jpf```
