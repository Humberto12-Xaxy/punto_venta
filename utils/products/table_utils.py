from flet import (
    Text,
    DataColumn,
    PopupMenuItem,
    icons,
    ControlEvent,
    Page
)

from models.product import Product

from controllers.product_controller import ProductController

from modules.products.widgets.modal_widget import ModalWidget

COLUMN_NAMES = [
    DataColumn(Text('ID', color='black')),
    DataColumn(Text('Name', color='black')),
    DataColumn(Text('Price', color='black')),
    DataColumn(Text('Stock', color='black')),
    DataColumn(Text('Code', color='black')),
    DataColumn(Text('Actions', color='black')),
]


def LIST_CELL_ACTIONS(id_product:int, product_controller: ProductController, page: Page) -> list:

    list_cell_actions = [
        PopupMenuItem(
            content=Text('Edit'),
            icon=icons.EDIT,
            on_click=lambda _: _update_products(page, product_controller.get_product_by_id(id_product)),
        ),
        PopupMenuItem(
            content=Text('Delete'),
            icon=icons.DELETE,
            on_click=lambda _: print('Delete') if product_controller.delete_product(id_product) else print('Error'),
        ),
    ]

    return list_cell_actions


def _update_products(page: Page, product: Product):
    modal = ModalWidget(page, product= product)
    page.open(modal)