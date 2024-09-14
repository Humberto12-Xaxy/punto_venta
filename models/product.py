

class Product:
    def __init__(self, name:str, price:float, stock:int, code:str):
        self._name = name
        self._price = price
        self._stock = stock
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        self._name = name
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price:float):
        self._price = price


    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock:int):
        self._stock = stock

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code:str):
        self._code = code
    
    def __str__(self):
        return f"Name: {self._name}, Price: {self._price}, Stock: {self._stock}, Code: {self._code}"