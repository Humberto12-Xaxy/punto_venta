

class DetailSale:

    def __init__(self, id_sale:int, id_product:int, count:int, unitario_price:float, subtotal:float):
        self._id_sale = id_sale
        self._id_product = id_product
        self._count = count
        self._unitario_price = unitario_price
        self._subtotal = subtotal
    
    @property
    def id_sale(self):
        return self._id_sale
    
    @id_sale.setter
    def id_sale(self, id_sale:int):
        self._id_sale = id_sale
    
    @property
    def id_product(self):
        return self._id_product
    
    @id_product.setter
    def id_product(self, id_product:int):
        self._id_product = id_product
    
    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, count:int):
        self._count = count
    
    @property
    def unitario_price(self):
        return self._unitario_price

    @unitario_price.setter
    def unitario_price(self, unitario_price:float):
        self._unitario_price = unitario_price
    
    @property
    def subtotal(self):
        return self._subtotal
    
    @subtotal.setter
    def subtotal(self, subtotal:float):
        self._subtotal = subtotal
    
    def __str__(self):
        return f"Id sale: {self._id_sale}, Id product: {self._id_product}, Count: {self._count}, Unitario price: {self._unitario_price}, Subtotal: {self._subtotal}"