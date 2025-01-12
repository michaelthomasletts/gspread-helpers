from __future__ import annotations

__all__ = ["RangeName"]

from attrs import define, field
from attrs.validators import ge, in_, instance_of, optional

from .validations import _validate_cols_arg, _validate_rows_arg


@define
class RangeName:
    """Generates a range name for updating a worksheet in Google Sheets or
    Excel, e.g. 'A1:B5'.

    Attributes
    ----------
    rows : int
        The number of total rows that should be updated in the worksheet.
        Value must be greater than zero. Value must also not exceed the
        predtermined limits set by the GOOGLE_SHEETS_ROW_LIMIT and-or
        EXCEL_ROW_LIMIT constants. Modulate the override_row_limit argument
        to supersede those limits. You may also modify the just-mentioned
        constants.
    cols : int
        The number of total columns that should be updated in the worksheet.
        Value must be greater than zero. Value must also not exceed the
        predtermined limits set by the GOOGLE_SHEETS_COL_LIMIT and-or
        EXCEL_COL_LIMIT constants. Modulate the override_col_limit argument
        to supersede those limits. You may also modify the just-mentioned
        constants.
    header_rows_size : int, optional
        If the rows and cols arguments do not account for a pre-existing
        header in the worksheet then use this parameter to indicate how large
        the header is, in terms of number of rows. Value must be equal to or
        greater than zero. Default is 0.
    source : ('google_sheets', 'excel'), optional
        Default is 'google_sheets'.
    override_row_limit : bool, optional
        Set to True if you would like to override the predetermined row limit.
        Default is False.
    override_col_limit : bool, optional
        Set to True if you would like to override the predetermined column
        limit. Default is False.
    range_name:
        Only accessible after the RangeName object is initialized. Generates
        the range name, e.g. 'A2:EE1000' per the provided arguments.

    Raises
    ------
    RowLimitExceeded : Exception
        Raised if the rows argument exceeds the predetermined limit set by
        the GOOGLE_SHEETS_ROW_LIMIT and EXCEL_ROW_LIMIT constants.
    ColumnLimitExceeded : Exception
        Raised if the cols argument exceeds the predetermined limit set by
        the GOOGLE_SHEETS_COL_LIMIT and EXCEL_COL_LIMIT constants.

    Examples
    --------
    The row limit for range names in Microsoft Excel is, by default, 1,048,576.
    Below, we override that limitation using the `override_col_limit` argument
    set to `True` and by setting `source` equal to 'excel'.

    >>> from gspread_helpers import RangeName
    >>> rn = RangeName(
    >>>     rows=2, cols=1_048_580, override_col_limit=True, source="excel"
    >>> )
    >>> print(rn.range_name)
    'A1:BGQCZ2'

    However, we could have also updated the `EXCEL_ROW_LIMIT` constant instead.

    >>> from gspread_helpers import EXCEL_ROW_LIMIT
    >>> EXCEL_ROW_LIMIT = 1_048_580
    >>> rn = RangeName(rows=2, cols=1_048_580, source="excel")
    >>> print(rn.range_name)
    'A1:BGQCZ2'

    Modulating the `header_rows_size` argument looks like this.

    >>> rn = RangeName(rows=2, cols=2, header_rows_size=2)
    'A3:B4'
    """

    rows: int = field(validator=[instance_of(int), ge(1), _validate_rows_arg])
    cols: int = field(validator=[instance_of(int), ge(1), _validate_cols_arg])
    header_rows_size: int = field(
        default=0, validator=optional([instance_of(int), ge(0)])
    )
    source: str = field(
        default="google_sheets",
        validator=optional(
            [instance_of(str), in_(["excel", "google_sheets"])]
        ),
    )
    override_row_limit: bool = field(default=False)
    override_col_limit: bool = field(default=False)

    def __attrs_post_init__(self):
        self.rows += self.header_rows_size

    @property
    def range_name(self) -> str:
        prefix = "".join(
            [
                "A",
                str(
                    1 + self.header_rows_size
                    if self.header_rows_size > 0
                    else 1
                ),
            ]
        )
        suffix, num_cols = "", self.cols

        while num_cols > 0:
            num_cols, remainder = divmod(num_cols - 1, 26)
            suffix = "".join([chr(65 + remainder), suffix])

        suffix = "".join([suffix, str(self.rows)])

        return ":".join([prefix, suffix])
