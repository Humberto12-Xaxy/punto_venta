import flet as ft

class MainView(ft.UserControl):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate
    
    def build(self):

        return ft.Column(
            [
                ft.Text('Home'),
                ft.ElevatedButton('Go to Products', on_click=self.go_to_products)
            ]
        )
    
    def go_to_products(self, e):
        self.on_navigate('/products')
