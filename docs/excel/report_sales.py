import os
import pandas as pd
from datetime import datetime

from models.sale import DataSale

from docs.pdfs.report_sales import get_documents_path

def dowload_excel(data_sales: list[DataSale]):

    documents_path = get_documents_path()
    file_path = os.path.join(documents_path, 'report.xlsx')

    df = pd.DataFrame()
    df['ID'] = [sale.id for sale in data_sales]
    df['Empleado'] = [sale.employee for sale in data_sales]
    df['Fecha'] = [ datetime.strptime(sale.date_sale, '%Y-%m-%d %H:%M').strftime('%d/%m/%Y %I:%M %p') for sale in data_sales]
    df['Total'] = [sale.total for sale in data_sales]

    with pd.ExcelWriter(file_path) as writer:
        df.to_excel(writer, index=False)
    
    return file_path
