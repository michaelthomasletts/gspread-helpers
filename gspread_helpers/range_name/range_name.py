from __future__ import annotations

__all__ = ["RangeName"]

from typing import Union

from attrs import define, field
from attrs.validators import ge, in_, instance_of, optional

from .validations import (
    _validate_buffer_arg,
    _validate_cols_arg,
    _validate_rows_arg,
)


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
    buffer : int | str, optional
        If you do not want to construct the range name beginning from the letter
        'A' then provide an integer or alphabetical letter that corresponds to the
        position with which you intend to begin constructing the range name.
    source : ('google_sheets', 'excel'), optional
        Default is 'google_sheets'.
    override_row_limit : bool, optional
        Set to True if you would like to override the predetermined row limit.
        Default is False.
    override_col_limit : bool, optional
        Set to True if you would like to override the predetermined column
        limit. Default is False.

    Other Attributes
    ----------------
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

    Finally, if we want to buffer the range name beginning from 'B', we may do
    this.

    >>> rn = RangeName(rows=2, cols=2, buffer=1)
    'B1:C2'

    Passing 'B' to `buffer` is equivalent to passing 1.

    >>> rn = RangeName(rows=2, cols=2, buffer="B")
    'B1:C2'
    """

    rows: int = field(validator=[instance_of(int), ge(1), _validate_rows_arg])
    cols: int = field(validator=[instance_of(int), ge(1), _validate_cols_arg])
    header_rows_size: int = field(
        default=0, validator=optional([instance_of(int), ge(0)])
    )
    buffer: Union[int | str] = field(
        default=0, validator=optional([_validate_buffer_arg])
    )
    source: str = field(
        default="google_sheets",
        validator=optional(
            [instance_of(str), in_(["excel", "google_sheets"])]
        ),
    )
    override_row_limit: bool = field(
        default=False, validator=instance_of(bool)
    )
    override_col_limit: bool = field(
        default=False, validator=instance_of(bool)
    )
    range_name: str = field(init=False)

    def __attrs_post_init__(self):
        self.buffer = (
            self.buffer.upper()
            if isinstance(self.buffer, str)
            else self.buffer
        )
        self.range_name = self._range_name()

    def _range_name(self) -> str:
        # creating prefix
        match (buffer_is_str := isinstance(self.buffer, str)):
            case True:
                prefix = self.buffer
            case False:
                prefix, _buffer = "", self.buffer
                while _buffer > 0:
                    _buffer, remainder = divmod(_buffer, 26)
                    prefix = "".join([chr(65 + remainder), prefix])

        prefix = "".join(
            [prefix if prefix else "A", str(1 + self.header_rows_size)]
        )

        # creating suffix
        suffix, num_cols = "", self.cols
        match buffer_is_str:
            case True:
                _buffer = 0
                for letter in self.buffer:
                    _buffer = _buffer * 26 + (ord(letter) - ord("A"))
            case False:
                _buffer = self.buffer

        while num_cols > 0:
            num_cols, remainder = divmod(num_cols - 1 + _buffer, 26)
            suffix = "".join([chr(65 + remainder), suffix])

        suffix = "".join([suffix, str(self.rows + self.header_rows_size)])

        return ":".join([prefix, suffix])
