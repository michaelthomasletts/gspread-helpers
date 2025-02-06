"""
Exceptions and Warnings (:mod:`gspread_helpers.range_name.exceptions`)
======================================================================

General exceptions used by `gspread_helpers.range_name`.

.. currentmodule:: gspread_helpers.range_name.exceptions

Exceptions
----------
.. autosummary::
    :toctree: range_name/

    RowLimitExceeded
    ColumnLimitExceeded
"""


class RowLimitExceeded(Exception):
    """Raised when rows parameter exceeds the row limit according to the source parameter."""

    ...


class ColumnLimitExceeded(Exception):
    """Raised when cols parameter exceeds the column limit according to the source parameter."""

    ...
