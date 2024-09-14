import flet
from flet import *

from database.create_table import create_table
from views.home.widgets.app_layout import AppLayout
from utils.main.app_bar_menu_actions import LIST_MENU_ACTIONS

create_table()

def main(page: Page):
    page.title = "Punto de Venta"
    page.window.maximized = True
    page.window.resizable = False

    page.appbar = AppBar(
        leading=Icon(icons.SHOPPING_CART, color="white"),
        title=Text("Punto de Venta"),
        actions=[
            Container(
                content=PopupMenuButton(items=LIST_MENU_ACTIONS),
                margin=margin.only(left=50, right=25),
            )
        ]
    )

    page.add(AppLayout(page))


flet.app(target=main)
