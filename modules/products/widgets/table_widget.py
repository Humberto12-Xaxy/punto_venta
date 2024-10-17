from flet import (
    DataTable,
    DataRow,
    DataCell,
    Page,
    Text,
    SnackBar,
    PopupMenuButton
)

from utils.products.table_utils import (
    COLUMN_NAMES,
    LIST_CELL_ACTIONS
)

from models.data_product import data_product
from models.product import Product


from controllers.product_controller import ProductController


class TableWidget(DataTable):
    def __init__(self, page: Page):
        super().__init__(
            columns=COLUMN_NAMES,
        )
        self.page = page

        self.load_products()

    def load_products(self):
        try:
            product_controller = ProductController()
            # Cargar productos nuevamente para evitar datos obsoletos
            for product in product_controller.get_all_products():
                self.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(str(product.id), color='black')),
                            DataCell(Text(product.name, color='black')),
                            DataCell(Text(f'${product.price}', color='black')),
                            DataCell(Text(str(product.stock), color='black')),
                            DataCell(Text(product.code, color='black')),
                            DataCell(
                                content=PopupMenuButton(
                                    items=LIST_CELL_ACTIONS(product.id, product_controller, self.page),
                                    tooltip= 'Mostrar opciones',
                                    )
                            ),
                        ],
                    )
                )
        except Exception as e:
            print(e)
            self.page.snack_bar = SnackBar(
                content=Text(
                    f'Error: No se pudo cargar los productos.', color='white'),
                bgcolor='red',
            )
            self.page.snack_bar.open = True
            self.page.update()
        finally:
            self.page.update()

    def update_table(self, list_products: list[Product]):
        self.rows.clear()
        product_controller = ProductController()
        for product in list_products:
            self.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(product.id), color='black')),
                        DataCell(Text(product.name, color='black')),
                        DataCell(Text(f'${product.price}', color='black')),
                        DataCell(Text(str(product.stock), color='black')),
                        DataCell(Text(product.code, color='black')),
                        DataCell(
                            content=PopupMenuButton(
                                items=LIST_CELL_ACTIONS(product.id, product_controller, self.page),
                                tooltip= 'Mostrar opciones',
                                )
                        ),
                    ],
                )
            )
        
        self.page.update()

