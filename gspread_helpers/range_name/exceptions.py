class RowLimitExceeded(Exception):
    """Raised when rows parameter exceeds the row limit according to the source parameter."""

    ...


class ColumnLimitExceeded(Exception):
    """Raised when cols parameter exceeds the column limit according to the source parameter."""

    ...
