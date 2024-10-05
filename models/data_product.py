
from models.product import Product

class DataProduct:

    def __init__(self) -> None:
        self.list_products: list[Product] = []
    
    def add_product(self, product:Product):
        self.list_products.append(product)
    
    def remove_product(self, product:Product):
        self.list_products.remove(product)
    
    def add_all_products(self, products:list):
        self.list_products.clear()
        self.list_products.extend(products)

    def get_list_products(self):
        return self.list_products
    
data_product = DataProduct()