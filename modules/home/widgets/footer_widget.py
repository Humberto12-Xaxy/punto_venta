from flet import (
    Page,
    Container,
    Row,
    Text,
    alignment,
    MainAxisAlignment,
    ElevatedButton,
)

from models.data_shop import data_shop

class FooterWidget(Row):

    def __init__(self, page: Page, subtotal: float):
        super().__init__()

        self.page = page
        self.subtotal = subtotal
        self.width = page.window.width * 0.8
        self.height = 100
        self.bgcolor = 'grey'
        self.expand = True

        self.alignment = MainAxisAlignment.SPACE_EVENLY

        self.controls = [
            self.total(),
        ]

    def total(self):
        
        return Container(
            width=410,
            height=75,
            bgcolor='#413D37',
            alignment=alignment.center,
            content=Text(f'Total: {self.subtotal}', size=20),
            border_radius= 50
        )

    def update_total(self, subtotal: float):
        self.subtotal = subtotal

        self.controls[0].content = Text(f'Total: ${self.subtotal}', size=20)

        self.page.update()