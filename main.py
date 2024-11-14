import flet
from flet import *

from database.create_table import create_table

from controllers.employee_controller import EmployeeController
from controllers.check_sqlite import check_sqlite

from router.main_router import Router


def main(page: Page):
    employee_controller = EmployeeController()

    
    page.title = "Punto de Venta"
    page.window.maximized = True
    page.window.resizable = False

    router = Router(page)

    def on_route_change(event: flet.RouteChangeEvent):
        router.route_change(event.route)



    page.on_route_change = on_route_change



    print(check_sqlite())

    if check_sqlite():
        create_table()
        page.go('/register')

    if len(employee_controller.get_all_employees()) > 0:
        page.go('/')

if __name__ == '__main__':
    flet.app(target=main)
