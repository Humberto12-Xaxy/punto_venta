import pandas as pd

from controllers.product_controller import ProductController


def upload_file(file_path: str):
    df = pd.read_excel(file_path)
    flag = False
    product_controller = ProductController()

    df = df.fillna('')
    
    for index, row in df.iterrows():
        price = float(row['precio']) if type(row['precio']) == float or type(row['precio']) == int else 0
        stock = int(row['cantidad']) if type(row['cantidad']) == int else 0
        code = str(row['codgo de barras']) if type(row['codgo de barras']) == int else 0

        if price != 0 and stock != 0 and code != 0:
            product = {
                'name': row['nombre'],
                'price': price,
                'stock': stock,
                'code': code
            }

            flag = product_controller.add_product(**product)
        else:
            flag = False
        
    return flag
        