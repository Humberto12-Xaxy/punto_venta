from flet import (
    Page,
    Container,
    Column,
    Text
)

from .widgets.header_widget import HeaderWidget
from .widgets.table_widget import TableWidget

class MainViewEmployees(Container):

    def __init__(self, page: Page):
        super().__init__()

        self.page = page

        self.bgcolor = 'white'

        self.width = page.window.width
        self.height = page.window.height

        self.table = TableWidget(self.page)

        self.content = Column(
            horizontal_alignment='center',
            controls=[
                HeaderWidget(self.page, self.table),
                self.table
            ]
        )