# gspread_helpers
[![PyPI Download](https://img.shields.io/pypi/v/gspread-helpers?logo=pypis.svg)](https://pypi.org/project/gspread-helpers/)
[![Workflow](https://img.shields.io/github/actions/workflow/status/michaelthomasletts/gspread-helpers/push_pullrequest.yml?logo=github)](https://github.com/michaelthomasletts/gspread-helpers/actions/workflows/push_pullrequest.yml)
![Python Version](https://img.shields.io/pypi/pyversions/gspread-helpers?style=pypi)

## Overview

A simple Python package which provides supplementary helper methods for [gspread](https://github.com/burnash/gspread).

## Features
- `gspread_helpers.RangeName` method for automatically generating dynamic range names, e.g. "A1:R455"

## Installation

```bash
$ pip install gspread-helpers
```

## Directory

```
gspread_helpers
├── __init__.py
└── range_name
    ├── __init__.py
    ├── exceptions.py
    ├── range_name.py
    └── validations.py
```

## Usage

The row limit for range names in Microsoft Excel is, by default, 1,048,576. Below, we override that limitation using the `override_col_limit` argument set to `True` and by setting `source` equal to 'excel'.

```python
from gspread_helpers import RangeName


rn = RangeName(
    rows=2, cols=1_048_580, override_col_limit=True, source="excel"
)
```

However, we could have also updated the `EXCEL_ROW_LIMIT` constant instead.

```python
from gspread_helpers import EXCEL_ROW_LIMIT


EXCEL_ROW_LIMIT = 1_048_580
rn = RangeName(rows=2, cols=1_048_580, source="excel")
```

Modulating the `header_rows_size` argument looks like this.

```python
rn = RangeName(rows=2, cols=2, header_rows_size=2)
```

Finally, if we want to buffer the range name beginning from 'B', we may do
this.

```python
rn = RangeName(rows=2, cols=2, buffer=1)
```

Passing 'B' to `buffer` is equivalent to passing 1.

```python
rn = RangeName(rows=2, cols=2, buffer="B")
```

## Contributing

Please refer to [contributing.md](https://github.com/michaelthomasletts/gspread-helpers/blob/main/docs/contributing.md) for step by step instructions for contributing to this project and understanding the coding standards before opening a pull request.