from __future__ import annotations

__all__ = [
    "GOOGLE_SHEETS_ROW_LIMIT",
    "EXCEL_ROW_LIMIT",
    "GOOGLE_SHEETS_COL_LIMIT",
    "EXCEL_COL_LIMIT",
]

from typing import Type

from .exceptions import ColumnLimitExceeded, RowLimitExceeded

GOOGLE_SHEETS_ROW_LIMIT = 10_000_000
EXCEL_ROW_LIMIT = 1_048_576
GOOGLE_SHEETS_COL_LIMIT = 18_278
EXCEL_COL_LIMIT = 16_384


def _validate_rows_arg(
    instance: Type["RangeName"], attribute: Type["Attribute"], value: int
):
    """Validates that the rows argument does not exceed platform limits per
    the source and override_row_limit arguments.

    Raises
    ------
    RowLimitExceeded : Exception
        Raised if the rows argument exceeds the predetermined limit set by
        the GOOGLE_SHEETS_ROW_LIMIT and EXCEL_ROW_LIMIT constants.
    """

    match instance.override_row_limit:
        case True:
            rows_limit = value
        case False:
            rows_limit = (
                GOOGLE_SHEETS_ROW_LIMIT
                if instance.source == "google_sheets"
                else EXCEL_ROW_LIMIT
            )

    if value > rows_limit:
        message = f"The row limit of {rows_limit} was exceeded by {value - rows_limit} rows!"
        raise RowLimitExceeded(message) from None


def _validate_cols_arg(
    instance: Type["RangeName"], attribute: Type["Attribute"], value: int
):
    """Validates that the cols argument does not exceed platform limits per
    the source and override_col_limit arguments.

    Raises
    ------
    ColumnLimitExceeded : Exception
        Raised if the cols argument exceeds the predetermined limit set by
        the GOOGLE_SHEETS_COL_LIMIT and EXCEL_COL_LIMIT constants.
    """

    match instance.override_col_limit:
        case True:
            cols_limit = value
        case False:
            cols_limit = (
                GOOGLE_SHEETS_COL_LIMIT
                if instance.source == "google_sheets"
                else EXCEL_COL_LIMIT
            )

    if value > cols_limit:
        message = f"The column limit of {cols_limit} was exceeded by {value - cols_limit} columns!"
        raise ColumnLimitExceeded(message) from None
