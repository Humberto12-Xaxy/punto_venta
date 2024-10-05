import os
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from datetime import datetime
import subprocess

from models.sale import DataSale


def get_documents_path():
    return str(Path.home() / 'Documents')

def generate_pdf(data_sales: list[DataSale]):
    
    documents_path = get_documents_path()
    file_path = os.path.join(documents_path, 'report.pdf')

    pdf = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    pdf.setFont('Helvetica-Bold', 16)
    pdf.drawString(100, height - 50, 'Reporte de Ventas')

    pdf.setFont('Helvetica', 12)
    pdf.drawString(50, height - 100, 'ID')
    pdf.drawString(150, height - 100, 'Empleado')
    pdf.drawString(250, height - 100, 'Fecha')
    pdf.drawString(410, height - 100, 'Total')

    y = height - 130
    for sale in data_sales:
        date = datetime.strptime(sale.date_sale, '%Y-%m-%d %H:%M')
        date = date.strftime('%d/%m/%Y %I:%M %p')

        pdf.drawString(50, y, str(sale.id))
        pdf.drawString(150, y, str(sale.employee))
        pdf.drawString(250, y, str(date))
        pdf.drawString(410, y, str(sale.total))
        y -= 20
    
    pdf.showPage()
    pdf.save()

    return file_path

def open_pdf(file_path: str):
    print(os.name)
    try:
        if os.name == 'nt':
            os.startfile(file_path)

        elif os.name == 'Darwin':
            subprocess.call(('open', file_path))

        elif os.name == 'posix':
            subprocess.call(('open', file_path))

        else:
            subprocess.call(('xdg-open', file_path))

    except Exception as e:
        print(e)