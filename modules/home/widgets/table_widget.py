from flet import (
    DataTable,
    DataRow,
    DataCell,
    Page,
    Text,
    ControlEvent,
    BorderSide,
    KeyboardEvent
)

from utils.home.table_utils import COLUMN_NAMES

from models.data_shop import data_shop, ProductShop
from models.product import Product


class TableWidget(DataTable):

    def __init__(self, page: Page):
        super().__init__(
            columns=COLUMN_NAMES,
        )
        self.vertical_lines = BorderSide(.3, 'black')
        self.width = page.window.width * 0.7
        self.height = page.window.height * 0.5
        self.page = page

    
    def update_table(self, list_products: list[ProductShop]):
        self.rows.clear()
        for product in list_products:
            self.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(product.name, color='black')),
                        DataCell(Text(f'${product.price}', color='black')), 
                        DataCell(Text(str(product.count), color='black')),
                    ],
                )
            )
        
        self.page.update()
