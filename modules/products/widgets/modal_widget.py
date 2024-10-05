from flet import (
    AlertDialog,
    Text,
    Page,
    TextButton,
    Column,
    Row,
    Container,
    alignment,
    MainAxisAlignment,
    ControlEvent,
    ButtonStyle,
    TextField,
    InputFilter,
    SnackBar
)

from models.product import Product

from controllers.product_controller import ProductController

class ModalWidget(AlertDialog):

    def __init__(self, page: Page, product: Product = None ):
        super().__init__()

        self.page = page
        self.modal = True
        self.title = Text('Añadir producto', color='black')

        self.bgcolor = 'white'

        self.product = product

        self.content = Column(
            height= self.page.height * 0.25,
            width= self.page.width * 0.7,
            alignment= MainAxisAlignment.SPACE_EVENLY,
            controls=[
                Row(
                    alignment= 'center',
                    controls=[
                        TextField(
                            width= self.page.width * 0.5,
                            label= 'Nombre del producto',
                            color= 'black',
                            value= product.name if product else '',
                        ),
                        TextField(
                            width= self.page.width * 0.1,
                            label= 'Precio',
                            color= 'black',
                            prefix_text= '$',
                            value= str(product.price) if product else '',
                            input_filter= InputFilter(
                                allow= True,
                                regex_string= r'^[0-9]*\.?[0-9]*$'
                            )
                        )
                    ]
                ),
                Row(
                    alignment= 'center',
                    controls=[
                        TextField(
                            width= self.page.width * 0.2,
                            label= 'Cantidad',
                            color= 'black',
                            value= str(product.stock) if product else '',
                            input_filter= InputFilter(
                                allow= True,
                                regex_string= r'^\d*$'
                            )
                        ),
                        TextField(
                            width= self.page.width * 0.4,
                            label= 'Código de barras',
                            color= 'black',
                            value= product.code if product else '',
                            input_filter= InputFilter(
                                allow= True,
                                regex_string= r'^\d*$'
                            ),
                            on_submit= self.add_product if not product else self.update_product
                        )
                    ]
                ),
            ]
        )

        self.actions = [
            TextButton(
                content=Text('Añadir' if not product else 'Actualizar'),
                style= ButtonStyle(color= 'green'),
                on_click=self.add_product if not product else self.update_product
            ),
            TextButton(
                content=Text('Cancelar'),
                on_click=self.close
            )
        ]

    
    def close(self, e: ControlEvent):
        self.page.close(self)
        self.content.controls[0].controls[0].value = ''
        self.content.controls[0].controls[1].value = ''
        self.content.controls[1].controls[0].value = ''
        self.content.controls[1].controls[1].value = ''
    
    def add_product(self, e: ControlEvent):
        name = self.content.controls[0].controls[0].value
        price = self.content.controls[0].controls[1].value
        stock = self.content.controls[1].controls[0].value
        code = self.content.controls[1].controls[1].value

        if name != '' and price != '' and stock != '' and code != '':
            product = {
                'name': name,
                'price': price,
                'stock': stock,
                'code': code
            }
            product_controller = ProductController()
            
            if product_controller:
                product_controller.add_product(**product)
                self.page.close(self)

            else:
                self.page.snack_bar = SnackBar(content=Text('No se pudo añadir el producto'))
                self.page.snack_bar.open = True
                self.page.update()
    
    def update_product(self, e: ControlEvent):
        name = self.content.controls[0].controls[0].value
        price = self.content.controls[0].controls[1].value
        stock = self.content.controls[1].controls[0].value
        code = self.content.controls[1].controls[1].value

        if name != '' and price != '' and stock != '' and code != '':
            product = {
                'id_product': self.product.id,
                'name': name,
                'price': price,
                'stock': stock,
                'code': code
            }
            product_controller = ProductController()
            
            if product_controller:
                product_controller.update_product(**product)
                self.page.close(self)

            else:
                self.page.snack_bar = SnackBar(content=Text('No se pudo actualizar el producto'))
                self.page.snack_bar.open = True
                self.page.update()