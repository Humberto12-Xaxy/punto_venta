from flet import (
    Page,
    Container,
    Row,
    ElevatedButton,
    icons,
    MainAxisAlignment,
    colors,
    TextField,
    FloatingActionButton
)

from .modal_widget import ModalWidget


class HeaderWidget(Row):
    def __init__(self, page: Page, table):
        super().__init__()

        self.page = page
        self.modal = ModalWidget(page, table)

        self.width = page.window.width
        self.alignment = MainAxisAlignment.END
        self.controls = [
            self.button_create_employee(),
            self.search_employee()
        ]

    def button_create_employee(self):
        return ElevatedButton(
            'Registrar',
            width=200,
            height=50,
            color='white',
            bgcolor='#495B6B',
            icon=icons.ADD,
            on_click= self.show_modal
        )
    
    def search_employee(self):
        return Row(
            controls=[
                TextField(
                    label='Buscar Empleado',
                    width=320,
                    height=50,
                    color=colors.BLACK,
                    autofocus=True,
                ),
                FloatingActionButton(
                    icon=icons.SEARCH,
                    width=40,
                    height=40,
                    bgcolor="#495B6B",
                )
            ]
        )

    def show_modal(self, e):
        self.page.open(self.modal)