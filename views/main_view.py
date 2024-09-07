import flet as ft
from flet import Text

class MainView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Punto de Venta"
        self.page.add(Text("Hello, Flet!"))