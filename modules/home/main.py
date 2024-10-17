from flet import (
    Page,
    Container,
    Column,
    MainAxisAlignment,
    KeyboardEvent,
    SnackBar,
    Text
)

from .widgets.search_widget import SeachWidget
from .widgets.table_widget import TableWidget
from .widgets.footer_widget import FooterWidget
from .widgets.modal_widget_home import ModalWidgetHome

from models.data_shop import data_shop

class MainView(Container):
    def __init__(self, page: Page):
        super().__init__()

        self.page = page

        self.modal = ModalWidgetHome(self.page, 0, 0)

        self.footer = FooterWidget(self.page, 0)

        # init table
        self.table = TableWidget(self.page)

        self.width = page.window.width 
        self.height = page.window.height
        self.padding = 10
        self.bgcolor = 'white'
        self.expand = True
        self.content = Column(
            alignment= MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                SeachWidget(page, self.table, self.footer),
                self.table,
                self.footer,
            ] 
        )

        self.page.on_keyboard_event = self.shortcut

    def shortcut(self, e: KeyboardEvent):
        text_field = self.content.controls[0].controls[0]
        
        
        if e.key == 'Enter' and text_field.value == '' and data_shop.get_list_products() and not self.modal.open:
            subtotal = self.footer.total().content.value
            print(subtotal)
            subtotal = subtotal.replace('Total: ', '')
            self.modal.update_subtotal(subtotal)
            self.page.open(self.modal)
            self.modal.open = True

        elif e.key == 'Escape' and self.modal.open:
            self.modal.open = False
            self.page.close(self.modal)
            text_field.focus()

        elif e.key == 'Backspace' and text_field.value == '' and data_shop.get_list_products() and not self.modal.open: 
            data_table = self.table.rows
            if data_table:
                self.table.rows.pop()
                data_shop.pop_product()
            else:
                self.page.snack_bar = SnackBar(
                    content=Text('No hay datos en la tabla', color='white'),
                    bgcolor='red',
                )
                self.page.snack_bar.open = True
            self.page.update()