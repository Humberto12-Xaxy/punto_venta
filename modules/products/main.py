from flet import (
    Page,
    Container,
    Column,
    ListView
)

from .widgets.header_widget import HeaderWidget
from .widgets.table_widget import TableWidget

from widgets.dt_pagination import DataTablePagination

class MainViewProducts(Container):
    def __init__(self, page: Page):
        super().__init__()

        self.page = page
        self.bgcolor = 'white'
        self.width = page.window.width * 0.85
        self.height = page.window.height

        self.table = TableWidget(page)

        self.table_pagination = DataTablePagination(page, self.table)
        self.content = Column(
            horizontal_alignment='center',
            controls=[
                HeaderWidget(page, self.table, self.table_pagination),
                self.table_pagination
            ]
        )
    