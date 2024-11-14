from flet import (
    Page,
    View,
    AppBar,
    Icon,
    Text,
    PopupMenuButton,
    Container,
    margin,
    icons
)


from utils.main.app_bar_menu_actions import GET_LIST_MENU_ACTIONS

from views.home.widgets.app_layout import AppLayout


class Home(View):
    def __init__(self, page: Page):
        super().__init__()

        self.page = page
        self.view = AppLayout(self.page)
        self.appbar = AppBar(
        bgcolor= '#2A91EB',
        leading=Icon(icons.SHOPPING_CART, color="white"),
        title=Text("Punto de Venta"),
        actions=[
            Container(
                content=PopupMenuButton(items=GET_LIST_MENU_ACTIONS(self.page)),
                margin=margin.only(left=50, right=25),
            )
        ]
    )
        self.controls = [
            self.view
        ]