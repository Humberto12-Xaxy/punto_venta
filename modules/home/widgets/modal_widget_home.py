from flet import (
    AlertDialog,
    Text,
    Page,
    TextButton,
    Column,
    Row,
    Container,
    alignment,
    MainAxisAlignment,
    ControlEvent,
    ButtonStyle,
    TextField,
    InputFilter
)

from datetime import datetime

from controllers.product_controller import ProductController
from controllers.sale_controller import SaleController
from controllers.detail_sale_controller import DetailSaleController

from models.data_shop import data_shop


class ModalWidgetHome(AlertDialog):
    def __init__(self, page: Page, total: float, change: float, table):
        super().__init__()

        self.page = page
        self.modal = True
        self.title = Text('Venta', color='black')

        self.table = table

        self.bgcolor = 'white'

        self.content = Column(
            height=self.page.height * 0.4,
            horizontal_alignment='center',
            alignment=MainAxisAlignment.SPACE_EVENLY,
            controls=[
                Row(
                    controls=[
                        Container(
                            alignment=alignment.center,
                            width=self.page.width * 0.15,
                            height=self.page.height * 0.07,
                            bgcolor='#413D37',
                            content=Text('Total:')
                        ),
                        Container(
                            alignment=alignment.center,
                            width=self.page.width * 0.15,
                            height=self.page.height * 0.07,
                            bgcolor='#413D37',
                            content=Text(str(total))
                        ),
                    ]
                ),
                TextField(
                    width=self.page.width * 0.35,
                    color='black',
                    autofocus=True,
                    label='Total recibido',
                    prefix_text='$',
                    input_filter=InputFilter(
                        allow=True,
                        regex_string=r'^\d*$'
                    ),
                    on_submit=self.on_submit,
                    on_change=lambda e: self.update_change(e.control.value)
                ),
                Row(
                    controls=[
                        Container(
                            alignment=alignment.center,
                            width=self.page.width * 0.15,
                            height=self.page.height * 0.07,
                            bgcolor='#413D37',
                            content=Text('Cambio:')
                        ),
                        Container(
                            alignment=alignment.center,
                            width=self.page.width * 0.15,
                            height=self.page.height * 0.07,
                            bgcolor='#413D37',
                            content=Text(f'${change}')
                        ),
                    ]
                ),
            ],
        )

        self.actions = [
            TextButton(
                'Confirmar',
                on_click=self.close,
                style=ButtonStyle(color='green'),
            ),
            TextButton(
                'Cancelar',
                on_click=self.close,
                style=ButtonStyle(color='blue')
            ),
        ]

    def close(self, e: ControlEvent):
        self.page.close(self)
        self.page.update()

    def update_subtotal(self, subtotal: float):
        self.subtotal = subtotal
        self.content.controls[0].controls[1].content = Text(f'${subtotal}')
        self.page.update()

    def update_change(self, total: float):
        subtotal = self.content.controls[0].controls[1].content.value.replace('$', '')
        change = float(total) - float(subtotal)
        if change > 0:
            self.content.controls[2].controls[1].content = Text(f'${change}')
        else:
            self.content.controls[2].controls[1].content = Text(f'${0}')
        self.page.update()

    def on_submit(self, e: ControlEvent):
        controller = ProductController()
        sale_controller = SaleController()
        detail_sale_controller = DetailSaleController()

        date = datetime.now().strftime('%Y-%m-%d %H:%M')

        id_sale = sale_controller.add_sale(date, self.subtotal, 4)

        for product in data_shop.get_list_products():
            controller.update_stock(product.id, product.stock - product.count)
            detail_sale_controller.add_detail_sale(id_sale, product.id, product.count, product.price, product.count * product.price)

        self.content.controls[1].focus()
        self.page.update()
        self.table.rows.clear()
        data_shop.clear_products()
        self.close(e)