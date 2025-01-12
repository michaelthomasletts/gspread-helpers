Overview
========

A simple Python package which provides supplementary helper methods for [gspread](https://github.com/burnash/gspread).

Presently, this package includes a single function for generating range names for updating worksheets in Google Sheets, e.g. 'A1:41209'. In the future, however, the intention is that additional methods will also be introduced.

Installation
============

```bash
$ pip install gspread-helpers
```

Directory
=========
```
gspread_helpers
├── __init__.py
└── range_name
    ├── __init__.py
    ├── exceptions.py
    ├── range_name.py
    └── validations.py
```

Usage
=====

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

Contributing
============
Please refer to [contributing.md](docs/contributing.md) for step by step instructions for contributing to this project and understanding the coding standards before opening a pull request.