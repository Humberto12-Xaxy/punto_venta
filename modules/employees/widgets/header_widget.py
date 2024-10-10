from flet import (
    Page,
    Container,
    Row,
    ElevatedButton
)

class HeaderWidget(Container):
    def __init__(self, page: Page):
        super().__init__()

        self.page = page

