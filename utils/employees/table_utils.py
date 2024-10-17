from flet import (
    Text,
    DataColumn,
    PopupMenuItem,
    Page,
    SnackBar
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


def LIST_CELL_ACTIONS(id:int, employee_controller: EmployeeController, page:Page, table):
    return [
        PopupMenuItem(
            text='Actualizar',
            on_click=lambda e: _update_employees(
                page, employee_controller.get_employee_by_id(id), table),
        ),
        PopupMenuItem(
            text='Eliminar',
            on_click=lambda _: _delete_employees(page, table, employee_controller, id),
        ),
    ]


def _delete_employees(page: Page, table, employee_controller: EmployeeController, id: int):
    if employee_controller.delete_employee(id):
        table.load_rows()
        page.snack_bar = SnackBar(
            Text('Usuario eliminado exitosamente', color='white'),
            bgcolor= 'green'
        )
        page.snack_bar.open = True
        page.update()
    else:
        page.snack_bar = SnackBar(
            Text('Error al eliminar el usuario', color='white'),
            bgcolor= 'red'
        )
        page.snack_bar.open = True
        page.update()

def _update_employees(page: Page, employee: Employee, table):
    modal = ModalWidget(page, table = table, employee = employee)
    page.open(modal)
