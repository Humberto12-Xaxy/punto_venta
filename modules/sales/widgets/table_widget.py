from flet import (
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    Page,
    Text,
    SnackBar,
    ControlEvent
)

from datetime import datetime

from models.sale import DataSale

from utils.sales.table_utils import COLUMN_NAMES

from controllers.sale_controller import SaleController
from .modal_widget_sale import ModalWidgetSale


class TableWidget(DataTable):
    def __init__(self, page: Page, modal: ModalWidgetSale):
        super().__init__(
            columns=COLUMN_NAMES,
            rows=[
            ],
        )

        self.page = page
        self.modal = modal
        self.load_sales()

        self.width = page.window.width * 0.7
        self.height = page.window.height

    def load_sales(self):
        try:
            self.rows.clear()
            sale_controller = SaleController()
            # Cargar ventas nuevamente para evitar datos obsoletos
            for sale in sale_controller.get_all_sales():
                date = datetime.strptime(sale.date_sale, '%Y-%m-%d %H:%M')
                date = date.strftime('%d/%m/%Y %I:%M %p')
                self.rows.append(
                    DataRow(
                        on_select_changed=lambda e, s=sale: self.open_modal(s),
                        cells=[
                            DataCell(Text(str(sale.id), color='black')),
                            DataCell(Text(sale.employee, color='black')),
                            DataCell(Text(date, color='black')),
                            DataCell(Text(sale.total, color='black')),
                        ],
                    )
                )
            self.page.update()

        except Exception as e:
            self.page.snack_bar = SnackBar(
                content=Text(
                    f'Error: No se pudo cargar las ventas.', color='white'),
                bgcolor='red',
            )
            self.page.snack_bar.open = True

    def open_modal(self, sale: DataSale): 
        self.modal.open = True
        self.modal.set_data(sale)
        self.page.open(self.modal)
