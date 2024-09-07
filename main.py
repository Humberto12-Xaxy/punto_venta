import flet 
from flet import *

from database.create_table import create_table
from router import Router
create_table()

def main(page: Page):
    page.title = "Punto de Venta"

    router = Router(page)

    def on_router_change(route):
        route = page.route
        router.handle_route_change(route)
    
    page.on_route_change = on_router_change
    page.go('/')


flet.app(target=main)