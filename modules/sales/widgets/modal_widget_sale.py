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
    CrossAxisAlignment,
    ControlEvent,
    ButtonStyle,
    TextField,
    InputFilter,
    TextThemeStyle,
    FontWeight,
    DataTable,
    DataRow,
    DataCell,
)

from datetime import datetime

from utils.sales.table_utils import COLUMN_NAMES_DETAILS

from controllers.detail_sale_controller import DetailSaleController

from models.sale import DataSale


class ModalWidgetSale(AlertDialog):

    def __init__(self, page: Page):
        super().__init__()

        self.page = page
        self.modal = True

        self.sale = None

        self.details_sale = []

        self.bgcolor = 'white'

        self.content = Column(
            width=self.page.width * 0.6,
            height=self.page.height * 0.7,
            horizontal_alignment='center',
            alignment=MainAxisAlignment.SPACE_AROUND,
            controls=[
                Text(
                    'Detalles de la Venta',
                    color='black',
                    weight=FontWeight.BOLD,
                    size=20,
                    theme_style=TextThemeStyle.TITLE_SMALL
                ),
                Container(
                    width=self.page.width * 0.5,
                    height=self.page.height * 0.2,
                    content=Column(
                        alignment=MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            Row(
                                controls=[
                                    Text('Vendido por: ', color='black'),
                                    Text('', color='black')
                                ]
                            ),
                            Row(
                                controls=[
                                    Text('Fecha: ', color='black'),
                                    Text('', color='black')
                                ]
                            ),
                        ]
                    )
                ),
                DataTable(
                    expand=True,
                    columns=COLUMN_NAMES_DETAILS,
                    rows=[],
                )
            ]
        )

        self.actions = [
            TextButton(
                text='Cerrar',

                on_click=self.close_dialog
            )
        ]

    def close_dialog(self, e: ControlEvent):
        self.page.close(self)
        self.page.update()

    def set_data(self, sale: DataSale):
        detail_sale_controller = DetailSaleController()

        date = datetime.strptime(sale.date_sale, '%Y-%m-%d %H:%M')
        date = date.strftime('%d/%m/%Y %I:%M %p')

        self.content.controls[1].content.controls[0].controls[1].value = sale.employee
        self.content.controls[1].content.controls[1].controls[1].value = date

        self.details_sale = detail_sale_controller.get_detail_sale_by_id_sale(
            id_sale=sale.id)
        
        self.content.controls[2].rows = []
        for detail_sale in self.details_sale:
            self.content.controls[2].rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(detail_sale.product_name) ,color='black')),
                        DataCell(Text(str(detail_sale.unitario_price), color='black')),
                        DataCell(Text(str(detail_sale.quantity), color='black')),
                        DataCell(Text(str(detail_sale.subtotal), color='black')),
                    ]
                )
            )
