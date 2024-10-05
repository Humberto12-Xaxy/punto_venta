from flet import(
    Page,
    Container,
    Text,
    Column,
    KeyboardEvent,
    ListView
)

from .widgets.table_widget import TableWidget
from .widgets.header_widget import HeaderWidgetSales
from .widgets.modal_widget_sale import ModalWidgetSale

from widgets.dt_pagination import DataTablePagination

class MainViewSales(Container):
    def __init__(self, page: Page):
        super().__init__()
        
        self.page = page
        self.bgcolor = 'white'
        self.width = page.window.width * 0.8
        self.height = page.window.height
        self.modal = ModalWidgetSale(self.page)
        self.table = TableWidget(page, self.modal)
        
        self.table_pagination = DataTablePagination(page, self.table)
        self.content = Column(
            horizontal_alignment='center',
            controls=[
                HeaderWidgetSales(self.page),
                self.table_pagination
            ]
        )

        self.page.on_keyboard_event = self.shortcut

        self.page.update()

    def shortcut(self, e: KeyboardEvent):
        
        if e.key == 'Escape' and self.modal.open:
            self.modal.open = False
            self.page.close(self.modal)
            self.page.update()
            