import flet
from flet import *

from database.create_table import create_table

from views.home.widgets.app_layout import AppLayout
from views.login.login import Login


from utils.main.app_bar_menu_actions import LIST_MENU_ACTIONS

from controllers.employee_controller import EmployeeController


def main(page: Page):
    employee_controller = EmployeeController()

    if len(employee_controller.get_all_employees()) == 0:
        create_table()
    
    page.title = "Punto de Venta"
    page.window.maximized = True
    page.window.resizable = False

    page.appbar = AppBar(
        visible= False,
        bgcolor= '#2A91EB',
        leading=Icon(icons.SHOPPING_CART, color="white"),
        title=Text("Punto de Venta"),
        actions=[
            Container(
                content=PopupMenuButton(items=LIST_MENU_ACTIONS),
                margin=margin.only(left=50, right=25),
            )
        ]
    )

    page.add(Login(page))

if __name__ == '__main__':
    flet.app(target=main)
