from flet import (
    DataColumn,
    Text
)

COLUMN_NAMES = [
    DataColumn(Text('ID', color='black')),
    DataColumn(Text('employee', color='black')),
    DataColumn(Text('Date', color='black')),
    DataColumn(Text('Total', color='black')),
]


COLUMN_NAMES_DETAILS = [
    DataColumn(Text('Product', color='black')),
    DataColumn(Text('Price', color='black')),
    DataColumn(Text('Count', color='black')),
    DataColumn(Text('Total', color='black')),
]