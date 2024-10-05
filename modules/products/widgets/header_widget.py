from flet import (
    Page,
    Row,
    ElevatedButton,
    FloatingActionButton,
    ControlEvent,
    Text,
    TextField,
    MainAxisAlignment,
    icons,
    colors,
    SnackBar,
    FilePicker,
    FilePickerResultEvent
)

from models.data_product import data_product

from widgets.dt_pagination import DataTablePagination

from .modal_widget import ModalWidget
from .table_widget import TableWidget

from docs.excel.upload_file import upload_file

from controllers.product_controller import ProductController

class HeaderWidget(Row):

    def __init__(self, page: Page, table: TableWidget, pagination: DataTablePagination):
        super().__init__()

        self.page = page
        self.width = page.window.width * 0.8

        self.pagination = pagination

        self.controller = ProductController()
        self.alignment = MainAxisAlignment.END

        self.modal = ModalWidget(page)
        self.table = table

        self.file_picker = FilePicker(
            on_result=self.upload_file,
        )
        self.page.overlay.append(self.file_picker)
        self.controls = [
            self.upload_excel(),
            self.create_new_product(),
            self.search_product()
        ]

        self.page.update()

    def create_new_product(self):
        return ElevatedButton(
            width=200,
            height=50,
            icon=  icons.ADD,
            text='Registrar',
            color='white',
            bgcolor='#495B6B',
            on_click=self.show_modal
        )
    
    def upload_excel(self):
        return ElevatedButton(
            width=200,
            height=50,
            text='Cargar Excel',
            icon=icons.UPLOAD_FILE,
            color='white',
            bgcolor='#495B6B',
            on_click= lambda e : self.file_picker.pick_files(allow_multiple = False)
        )

    def search_product(self):
        return Row(
            controls=[
                TextField(
                    label='Buscar Producto',
                    width=320,
                    height=50,
                    color=colors.BLACK,
                    autofocus=True,
                    on_submit=self.search
                ),
                FloatingActionButton(
                    icon=icons.SEARCH,
                    width=40,
                    height=40,
                    bgcolor="#495B6B",
                    on_click=self.search
                )
            ]
        )
    
    def search(self, e: ControlEvent):
        if e.name == 'submit':
            products = self.controller.get_products_by_name(e.data)
            data_product.add_all_products(products)
            self.controls[2].controls[0].value = ''
            self.controls[2].controls[0].focus()
        elif e.name == 'click':
            text = self.controls[2].controls[0].value
            products = self.controller.get_products_by_name(text)
            data_product.add_all_products(products)
            self.controls[2].controls[0].value = ''
            self.controls[2].controls[0].focus()

        if not products:
            self.page.snack_bar = SnackBar(
                content=Text('No se encontraron resultados'),
            )
            self.page.snack_bar.open = True
            data_product.add_all_products(self.controller.get_all_products()) 

        
        self.table.update_table(data_product.get_list_products())
        self.pagination.data_rows = self.table.rows
        self.page.update()

    def show_modal(self, e: ControlEvent):
        self.page.open(self.modal)

    
    def upload_file(self, e: FilePickerResultEvent):
        if e.files[0].name.endswith('.xlsx'):
            path = e.files[0].path
            flag = upload_file(path)

            if flag:
                self.page.snack_bar = SnackBar(
                    content=Text('Archivo cargado exitosamente',color='white'),
                    bgcolor='green',
                )
                self.page.snack_bar.open = True
                self.page.update()
            else:
                self.page.snack_bar = SnackBar(
                    content=Text('Hubo un error al cargar el archivo', color='white'),
                    bgcolor='red',
                )
                self.page.snack_bar.open = True
                self.page.update()
        
        else:
            self.page.snack_bar = SnackBar(
                content=Text('El archivo debe ser de tipo .xlsx'),
            )
            self.page.snack_bar.open = True
            self.page.update()
