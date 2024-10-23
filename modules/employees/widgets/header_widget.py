from flet import (
    Page,
    Text,
    SnackBar,
    Row,
    ElevatedButton,
    icons,
    MainAxisAlignment,
    colors,
    TextField,
    FloatingActionButton,
    ControlEvent
)

from controllers.employee_controller import EmployeeController

from .modal_widget import ModalWidget

from widgets.dt_pagination import DataTablePagination


class HeaderWidget(Row):
    def __init__(self, page: Page, table_pagination: DataTablePagination, table):
        super().__init__()

        self.page = page
        self.modal = ModalWidget(page, table_pagination = table_pagination, table = table)

        self.controller = EmployeeController()
        self.table = table
        self.pagination = table_pagination

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
                    on_submit=self.search
                ),
                FloatingActionButton(
                    icon=icons.SEARCH,
                    width=40,
                    height=40,
                    bgcolor="#495B6B",
                    on_click=self.search
                )
            ]
        )

    def show_modal(self, e):
        self.page.open(self.modal)

    def search(self, e:ControlEvent):
        if e.name == 'submit':
            employees = self.controller.get_employees_by_name(e.data)
            self.controls[1].controls[0].value = ''
            self.controls[1].controls[0].focus()
        elif e.name == 'click':
            text = self.controls[1].controls[0].value
            employees = self.controller.get_employees_by_name(text)
            self.controls[1].controls[0].value = ''
            self.controls[1].controls[0].focus()

        
        if not employees:
            self.page.snack_bar = SnackBar(
                content=Text('No se encontraron resultados'),
            )
            self.page.snack_bar.open = True
        
        self.table.update_table(employees)
        self.pagination.data_rows = self.table.rows
        self.page.update()