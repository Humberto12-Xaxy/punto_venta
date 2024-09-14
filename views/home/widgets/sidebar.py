from flet import (
    icons,
    Container,
    Page,
    Column,
    Row,
    NavigationRail,
    colors,
    Text,
    margin,
    padding,
    ControlEvent
    )

from utils.main.navigation_rail_setting import NAVIGATION_RAIL_SETTINGS
from router.router import Router

class Sidebar(Container):

    def __init__(self, app_layout: Row, page: Page):
        super().__init__()

        self.app_layout = app_layout
        self.page = page

        self.nav_rail = NavigationRail(
            height=self.page.window.height,
            label_type=NAVIGATION_RAIL_SETTINGS['label_type'],
            selected_index=NAVIGATION_RAIL_SETTINGS['selected_index'],
            destinations=NAVIGATION_RAIL_SETTINGS['destinations'],
            extended=True,
            expand=True,
            on_change= self.on_change
        )

        self.content = Column(      
            controls=[
                self.nav_rail
            ],
            tight= True
        )
    
    def on_change(self, e: ControlEvent):
        router = Router(self.page)

        self.nav_rail.selected_index = e.control.selected_index
        if e.control.selected_index == 0:
            self.app_layout.view.content = router.load_home()
        elif e.control.selected_index == 1:
            self.app_layout.view.content = router.load_products()
        elif e.control.selected_index == 2:
            self.app_layout.view.content = router.sales()
        self.app_layout.update()
        self.page.update()