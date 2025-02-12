"""
Exceptions and Warnings (:mod:`gspread_helpers.range_name.exceptions`)
======================================================================

General exceptions used by ``gspread_helpers.range_name``.
"""


class RowLimitExceeded(Exception):
    """Raised when rows parameter exceeds the row limit according to the source parameter."""

    ...


class ColumnLimitExceeded(Exception):
    """Raised when cols parameter exceeds the column limit according to the source parameter."""

    ...
