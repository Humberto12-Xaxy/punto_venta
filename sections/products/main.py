import flet as ft

class MainViewProducts(ft.UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        return ft.Column(
            [
                ft.Text('Products'),
            ]
        )