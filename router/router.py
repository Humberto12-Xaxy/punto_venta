import flet as ft 

from sections.home.main import MainView
from sections.products.main import MainViewProducts


class Router:
    def __init__(self, page: ft.Page):
        self.page = page

    def load_home(self):
        home_view = MainView(self.page)
        return home_view
    
    def load_products(self):
        products_view = MainViewProducts()
        return products_view
    
    def sales(self):
        sales_view = ft.Column()
        return sales_view