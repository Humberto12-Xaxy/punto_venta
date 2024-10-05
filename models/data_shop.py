from models.product import Product
from models.product_shop import ProductShop

class DataShop:
    def __init__(self) -> None:
        self.list_products: list[ProductShop] = []

    def add_product(self, product:Product, count:int = 0):
        count_product = 1
        flag = False

        for product_ in self.list_products:
            if product_.id == product.id:
                product_.count += count_product
                flag = True
                
        if not flag:
            product_shop = ProductShop(product.id, product.name, product.price, product.stock, product.code, count)
            self.list_products.append(product_shop)

    def get_list_products(self):
        return self.list_products
    
    def remove_product(self, product):
        self.list_products.remove(product)

    def pop_product(self):
        self.list_products.pop()

data_shop = DataShop()