from flet import (
    Page,
    Row,
    ElevatedButton,
    ControlEvent,
    SnackBar,
    Text,
    MainAxisAlignment,
    icons
)

from controllers.sale_controller import SaleController

from docs.pdfs.report_sales import generate_pdf, open_pdf
from docs.excel.report_sales import dowload_excel

class HeaderWidgetSales(Row):

    def __init__(self, page: Page):
        super().__init__()

        self.page = page
        self.modal = True

        self.bgcolor = 'white'

        self.width = page.window.width * 0.8
        self.alignment = MainAxisAlignment.END

        self.controls = [
            self.button_download_excel(),
            self.button_download_pdf()
        ]

    def button_download_pdf(self):
        return ElevatedButton(
            text='Descargar PDF',
            color='white',
            icon= icons.PICTURE_AS_PDF,
            bgcolor='#495B6B',
            width=200,
            height=50,
            on_click=self.download_pdf,
        )
    
    def button_download_excel(self):
        return ElevatedButton(
            text='Descargar Excel',
            color='white',
            icon= icons.FILE_DOWNLOAD,
            bgcolor='#495B6B',
            width=200,
            height=50,
            on_click=self.download_excel,
        )
    
    def download_pdf(self, event: ControlEvent):
        
        sale_controller = SaleController()

        pdf_path = generate_pdf(sale_controller.get_all_sales())


        self.page.snack_bar = SnackBar(
            content=Text(f'PDF descargado en {pdf_path}', color='white'),
            bgcolor='#495B6B',
        )

        self.page.snack_bar.open = True
        self.page.update()

        open_pdf(pdf_path)
    
    def download_excel(self, event: ControlEvent):
        
        sale_controller = SaleController()

        data_sales = sale_controller.get_all_sales()

        file_path = dowload_excel(data_sales)

        self.page.snack_bar = SnackBar(
            content=Text(f'Excel descargado en {file_path}', color='white'),
            bgcolor='#495B6B',
        )

        self.page.snack_bar.open = True
        self.page.update()

        open_pdf(file_path)