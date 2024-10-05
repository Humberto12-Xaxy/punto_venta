
class Sale:

    def __init__(self, id:int = None, date_sale:str = '', total:float = 0.0, id_employee:int = 0):
        self._id = id
        self._date_sale = date_sale
        self._total = total
        self._id_employee = id_employee

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id:int):
        self._id = id
    
    @property
    def date_sale(self):
        return self._date_sale
    
    @date_sale.setter
    def date_sale(self, date_sale:str):
        self._date_sale = date_sale
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, total:float):
        self._total = total
    
    @property
    def id_employee(self):
        return self._id_employee
    
    @id_employee.setter
    def id_employee(self, id_employee:int):
        self._id_employee = id_employee
    
    def __str__(self):
        return f"Date: {self._date_sale}, Total: {self._total}, Employee: {self._id_employee}"
    
class DataSale:
    def __init__(self, id:int, date_sale:str, total:float, employee:str):
        self._id = id
        self._date_sale = date_sale
        self._total = total
        self._employee = employee
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id:int):
        self._id = id
    
    @property
    def date_sale(self):
        return self._date_sale
    
    @date_sale.setter
    def date_sale(self, date_sale:str):
        self._date_sale = date_sale
    
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total:float):
        self._total = total
    
    @property
    def employee(self):
        return self._employee
    
    @employee.setter
    def employee(self, employee:int):
        self._employee = employee

    def __str__(self):
        return f"ID: {self._id}, Date: {self._date_sale}, Total: {self._total}, Employee: {self._employee}"