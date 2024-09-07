import flet as ft 

from views.home.main import MainView


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            '/': self.load_home,
        }
    
    def handle_route_change(self, route):
        if route in self.routes:
            self.routes[route]()
        else:
            self.page.add(ft.Text(f"Route {route} not found"))
    
    def load_home(self):
        self.page.views.clear()
        home_view = MainView(self.page.go)
        self.page.add(home_view)
        self.page.update()
    
    def load_products(self):
        pass