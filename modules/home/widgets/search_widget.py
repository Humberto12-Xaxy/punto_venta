from flet import (
    Page,
    TextField,
    Row,
    icons,
    colors,

    FloatingActionButton,
    ControlEvent
)

# data
from models.data_shop import data_shop

from controllers.product_controller import ProductController

from .table_widget import TableWidget
from .footer_widget import FooterWidget

class SeachWidget(Row):

    def __init__(self, page: Page, table: TableWidget, footer: FooterWidget):
        super().__init__()

        self.page = page
        self.table = table
        self.footer = footer
        self.product_controller = ProductController()

        self.width = page.window.width
        self.height = 40
        self.alignment = 'end'
        self.expand = True

        self.controls = [
            TextField(
                width=500,
                height=50,
                color=colors.BLACK,
                autofocus=True,
                on_submit= self.search
            ),
            FloatingActionButton(
                icon=icons.SEARCH,
                width=40,
                height=40,
                bgcolor="#495B6B",
                on_click= self.search
            )
        ]

        self.page.update()

    def search(self, e: ControlEvent):
        code:str = self.controls[0].value
        subtotal = 0
        quantity = 0

        if '*' in code:
            quantity = code.split('*')[0]
            code = code.split('*')[1]

        if code != '':
            data_product = self.product_controller.get_product_by_code(code)
            if data_product:
                data_shop.add_product(data_product, int(quantity) if int(quantity) != 0 else 1)
                self.table.update_table(data_shop.get_list_products())
                subtotal = sum([product.price * product.count for product in data_shop.get_list_products()])
                self.footer.update_total(subtotal)
            else:
                print('No se encontraron resultados')
                
        self.controls[0].value = ''
        self.controls[0].focus()