from flet import (
    Page,
    View
)


from views.login.login import Login
from views.home.home import Home
from views.register.register import RegisterView


class Router:
    def __init__(self, page: Page):
        self.page = page
        
    def route_change(self, route: str):
        self.routes = {
            '/': View(controls=[Login(self.page)]),
            '/register': RegisterView(self.page),
            '/main': Home(self.page),
        }

        if route in self.routes:
            self.page.views.clear()
            self.page.views.append(
                self.routes[route]
            )
            self.page.update()
