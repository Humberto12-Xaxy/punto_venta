from flet import (
    Row,
    Container,
    colors,
    padding,
    transform,
    animation,
    Page,
    Text,
    View
)

from .sidebar import Sidebar

from modules.home.main import MainView


class AppLayout(Row):

    def __init__(self, page: Page):
        super().__init__()

        self.page = page
        self.view = MainView(self.page)

        self.expand = True

        self.controls = [
            Sidebar(self, self.page),
            self.view
        ]