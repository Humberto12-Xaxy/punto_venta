from flet import (
    Text,
    DataColumn,
    PopupMenuItem,
    Page
)

from controllers.employee_controller import EmployeeController

from models.employee import Employee

from modules.employees.widgets.modal_widget import ModalWidget

COLUMN_NAMES = [
    DataColumn(Text('Name', color='black')),
    DataColumn(Text('username', color='black')),
    DataColumn(Text('rol', color='black')),
    DataColumn(Text('Actions', color='black')),
]


def LIST_CELL_ACTIONS(id, employee_controller: EmployeeController, page, table):
    return [
        PopupMenuItem(
            text='Actualizar',
            on_click=lambda e: _update_employees(page, employee_controller.get_employee_by_id(id), table),
        ),
        PopupMenuItem(
            text='Eliminar',
            on_click=lambda _: print('Delete') if employee_controller.delete_employee(id) else print('Error'),
        ),
        ]

def _update_employees(page: Page, employee: Employee, table):
    modal = ModalWidget(page, table, employee)
    page.open(modal)