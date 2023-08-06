# dead_function_finder

[![Build Status](https://github.com/gabfl/dead_function_finder/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/gabfl/dead_function_finder/actions)
[![codecov](https://codecov.io/gh/gabfl/dead_function_finder/branch/main/graph/badge.svg)](https://codecov.io/gh/gabfl/dead_function_finder)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/gabfl/dead_function_finder/main/LICENSE)

Utility to find dead functions within a codebase.

## Languages supported

 - Python
 - PHP

## Installation

### Using PIP

```bash
pip3 install dead_function_finder
```

### From sources

```bash
git clone https://github.com/gabfl/dead_function_finder.git && cd dead_function_finder
pip3 install .
```

## Usage

```bash
dead_function_finder --path "~/my/codebase" --language python

# Specific patterns can be excluded with --exclude:
dead_function_finder --path "~/my/codebase" --language python --exclude '/venv/,/unittest/'
```

## Limitations

 - The program searches for unique function names; it is not currently aware of class context.
 - Functions called with magic methods or whose names are dynamically resolved might result in false positives.
