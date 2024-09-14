
class Sale:

    def __init__(self, date_sale:str, total:float, id_employee:int):
        self._date_sale = date_sale
        self._total = total
        self._id_employee = id_employee
    
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