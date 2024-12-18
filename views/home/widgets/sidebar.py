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

from utils.main.navigation_rail_setting import NAVIGATION_RAIL_SETTINGS, create_navigation_rail
from router.router import Router

class Sidebar(Container):

    def __init__(self, app_layout: Row, page: Page):
        super().__init__()

        self.app_layout = app_layout
        self.page = page

        self.router = Router(self.page)
        
        print('privileges', self.page.client_storage.get('privileges'))

        self.nav_rail = NavigationRail(
            bgcolor= '#497DAB',
            height=self.page.window.height,
            label_type=NAVIGATION_RAIL_SETTINGS['label_type'],
            selected_index=NAVIGATION_RAIL_SETTINGS['selected_index'],
            destinations= create_navigation_rail(self.page),
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

        self.nav_rail.selected_index = e.control.selected_index
        if e.control.selected_index == 0:
            self.app_layout.view.content = self.router.load_home()
        elif e.control.selected_index == 1:
            self.app_layout.view.content = self.router.load_products()
        elif e.control.selected_index == 2:
            self.app_layout.view.content = self.router.sales()
        elif e.control.selected_index == 3:
            self.app_layout.view.content = self.router.employees()
        self.app_layout.update()
    