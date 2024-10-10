from flet import (
    Page,
    Container,
    Column,
    Text
)

class MainViewEmployees(Container):

    def __init__(self, page: Page):
        super().__init__()

        self.page = page

        self.bgcolor = 'white'

        self.width = page.window.width * 0.85

        self.content = Column(
            horizontal_alignment='center',
            controls=[
                Text('Empleados')
            ]
        )