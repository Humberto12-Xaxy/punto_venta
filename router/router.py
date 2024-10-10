import flet as ft 

from modules.home.main import MainView
from modules.products.main import MainViewProducts
from modules.sales.main import MainViewSales
from modules.employees.main import MainViewEmployees

class Router:
    def __init__(self, page: ft.Page):
        self.page = page

    def load_home(self):
        home_view = MainView(self.page)
        return home_view
    
    def load_products(self):
        products_view = MainViewProducts(self.page)
        return products_view
    
    def sales(self):
        sales_view = MainViewSales(self.page)
        return sales_view
    
    def employees(self):
        employees_view = MainViewEmployees(self.page)
        return employees_view