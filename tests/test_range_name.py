from pytest import mark

from gspread_helpers.range_name.range_name import RangeName


@mark.imports
def test_range_name_validations_all_import():
    from gspread_helpers.range_name.validations import __all__ as a

    assert sorted(a) == sorted(
        [
            "GOOGLE_SHEETS_ROW_LIMIT",
            "EXCEL_ROW_LIMIT",
            "GOOGLE_SHEETS_COL_LIMIT",
            "EXCEL_COL_LIMIT",
        ]
    )


@mark.imports
def test_range_name_range_name_all_import():
    from gspread_helpers.range_name.range_name import __all__ as a

    assert a == ["RangeName"]


@mark.imports
def test_range_name_all_import():
    from gspread_helpers.range_name import __all__ as a

    assert sorted(a) == sorted(
        [
            "RangeName",
            "GOOGLE_SHEETS_ROW_LIMIT",
            "EXCEL_ROW_LIMIT",
            "GOOGLE_SHEETS_COL_LIMIT",
            "EXCEL_COL_LIMIT",
        ]
    )


@mark.imports
def test_all_import():
    from gspread_helpers import __all__ as a

    assert sorted(a) == sorted(
        [
            "range_name",
            "RangeName",
            "GOOGLE_SHEETS_ROW_LIMIT",
            "EXCEL_ROW_LIMIT",
            "GOOGLE_SHEETS_COL_LIMIT",
            "EXCEL_COL_LIMIT",
        ]
    )


@mark.imports
def test_misc_imports():
    from gspread_helpers import (
        EXCEL_COL_LIMIT,
        EXCEL_ROW_LIMIT,
        GOOGLE_SHEETS_COL_LIMIT,
        GOOGLE_SHEETS_ROW_LIMIT,
        range_name,
    )


@mark.exceptions
def test_rows():
    try:
        rn = RangeName(rows=1, cols=0)
    except ValueError:
        ...


@mark.exceptions
def test_cols():
    try:
        rn = RangeName(rows=0, cols=1)
    except ValueError:
        ...


@mark.exceptions
def test_header_rows_size():
    rn = RangeName(rows=1, cols=1)
    assert rn.header_rows_size == 0


@mark.exceptions
def test_source():
    rn = RangeName(rows=1, cols=1)
    assert rn.source == "google_sheets"

    try:
        rn = RangeName(rows=1, cols=1, source="test")
    except ValueError:
        ...


@mark.exceptions
def test_override_col_limit():
    rn = RangeName(rows=1, cols=1)
    assert rn.override_col_limit is False


@mark.exceptions
def test_override_row_limit():
    rn = RangeName(rows=1, cols=1)
    assert rn.override_row_limit is False


@mark.functions
def test_range_name():
    # testing basic functionality
    correct_range_name = "A1:B2"
    range_name = RangeName(rows=2, cols=2)
    assert correct_range_name == range_name.range_name

    # testing basic functionality with an IRL example
    df = [[0, 1], [1, 2], [5, 10]]
    correct_range_name = "A1:B3"
    range_name = RangeName(rows=len(df), cols=len(df[0]))
    assert correct_range_name == range_name.range_name

    # testing header_rows_size
    correct_range_name = "A3:B4"
    range_name = RangeName(rows=2, cols=2, header_rows_size=2)
    assert correct_range_name == range_name.range_name

    # testing override row limit for Google Sheets
    correct_range_name = "A1:B10000001"
    range_name = RangeName(rows=10_000_001, cols=2, override_row_limit=True)
    assert correct_range_name == range_name.range_name

    # testing override col limit for Google Sheets
    correct_range_name = "A1:BUYB2"
    range_name = RangeName(rows=2, cols=50_000, override_col_limit=True)
    assert correct_range_name == range_name.range_name

    # testing override row limit for Excel
    correct_range_name = "A1:B10000001"
    range_name = RangeName(
        rows=10_000_001, cols=2, override_row_limit=True, source="excel"
    )
    assert correct_range_name == range_name.range_name

    # testing override col limit for Excel
    correct_range_name = "A1:BGQCZ2"
    range_name = RangeName(
        rows=2, cols=1_048_580, override_col_limit=True, source="excel"
    )
    assert correct_range_name == range_name.range_name
