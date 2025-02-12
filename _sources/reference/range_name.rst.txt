.. _range_name:

.. currentmodule:: gspread_helpers.range_name

gspread_helpers.range_name
**************************

The following submodules contain methods for generating dynamic range names, i.e. 'A2:C59'.

For examples, please refer to the `Examples` section of an individual class or function.

Submodules
----------
.. autosummary::
    :toctree: range_name/

    exceptions
    range_name
    validations

Usage
-----

The row limit for range names in Microsoft Excel is, by default, 1,048,576.
Below, we override that limitation using the ``override_col_limit`` argument
set to ``True`` and by setting ``source`` equal to 'excel'.

.. code-block:: python

    from gspread_helpers import EXCEL_ROW_LIMIT, RangeName
    
    rn = RangeName(
        rows=2, cols=2, override_col_limit=True, source="excel"
    )

However, we could have also modulated the ``EXCEL_ROW_LIMIT`` constant instead.

.. code-block:: python

    EXCEL_ROW_LIMIT = 1_048_580
    rn = RangeName(rows=2, cols=1_048_580, source="excel")
    print(rn.range_name)

Modulating the ``header_rows_size`` argument looks like this, and returns 'A3:B4'.

.. code-block:: python

    rn = RangeName(rows=2, cols=2, header_rows_size=2)

Finally, if we want to buffer the range name beginning from 'B', we may do
this, which returns 'B1:C2'

.. code-block:: python

    rn = RangeName(rows=2, cols=2, buffer=1)

Passing 'B' to ``buffer`` is equivalent to passing 1, and returns 'B1:C2'.

.. code-block:: python
    
    rn = RangeName(rows=2, cols=2, buffer="B")