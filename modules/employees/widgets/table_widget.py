from flet import (
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    Page,
    Text,
    SnackBar,
    ControlEvent,
    PopupMenuButton
)


from models.employee import Employee

from utils.employees.table_utils import COLUMN_NAMES
from utils.employees.table_utils import LIST_CELL_ACTIONS

from controllers.employee_controller import EmployeeController


class TableWidget(DataTable):
    def __init__(self, page: Page):
        super().__init__(
            columns=COLUMN_NAMES,
        )
        self.page = page
        self.width = page.window.width * 0.7

        self.employee_controller = EmployeeController()

        self.load_rows()

    def load_rows(self):
        self.rows.clear()
        list_employees = self.employee_controller.get_all_employees()
        for employee in list_employees:
            self.rows.append(
                DataRow(cells=[
                    DataCell(Text(employee.name, color='black')),
                    DataCell(Text(employee.username, color='black')),
                    DataCell(Text(employee.rol, color='black')),
                    DataCell(
                        content=PopupMenuButton(
                            items = LIST_CELL_ACTIONS(employee.id, self.employee_controller, self.page, self),
                        tooltip='Actualizar | Eliminar',
                    )),
                ]))

        self.page.update()
            
    def update_table(self, list_employees: list[Employee]):
        self.rows.clear()
        for employee in list_employees:
            self.rows.append(
                DataRow(cells=[
                    DataCell(Text(employee.name, color='black')),
                    DataCell(Text(employee.username, color='black')),
                    DataCell(Text(employee.rol, color='black')),
                    DataCell(
                        content=PopupMenuButton(
                            items = LIST_CELL_ACTIONS(employee.id, self.employee_controller, self.page, self),
                        tooltip='Actualizar | Eliminar',
                    )),
                ]))
            
        self.page.update()
