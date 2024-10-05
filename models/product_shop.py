from models.product import Product

class ProductShop(Product):
    def __init__(self, id:int = None, name:str = '', price:float = 0.0, stock:int = 0, code:str = '', count:int = 0):
        super().__init__(id, name, price, stock, code)
        self._count = count

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count:int):
        self._count = count

    def __str__(self):
        return f"Id: {self._id}, Name: {self._name}, Price: {self._price}, Stock: {self._stock}, Code: {self._code}, Count: {self._count}"