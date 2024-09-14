from flet import (
    Page,
    Container,
    Row,
    Column,
    Text
)

from .widgets.search_widget import SeachWidget

class MainView(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.width = page.window.width
        self.height = page.window.height
        self.content = Column(
            expand=True,
            
            controls=[
                SeachWidget(page),
                Text("Home")
            ]
        )
