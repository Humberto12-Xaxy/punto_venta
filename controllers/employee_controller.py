from database.database_connection import DatabaseConnection
from models.employee import Employee

class EmployeeController:
    def __init__(self):
        self._db = DatabaseConnection().connection("db.sqlite3")
    
    def get_all_employees(self):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM employees')
            employees = cursor.fetchall()
            employees = [Employee(*employee) for employee in employees]
            cursor.close()
            return employees

    def get_employee_by_id(self, id_employee:int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM employees WHERE id = ?', (id_employee,))
        employee = cursor.fetchone()
        cursor.close()
        self._db.close()
        return Employee(*employee)

    def add_employee(self, name:str, username:str, password:str, rol:str):
        cursor = self._db.cursor()
        cursor.execute('INSERT INTO employees VALUES (?,?,?,?,?)', (None, name, username, password, rol))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True

    def update_employee(self, id_employee:int, name:str, username:str, password:str, rol:str):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM employees WHERE id = ?', (id_employee,))
        employee = cursor.fetchone()
        if not employee:
            return False
        cursor.execute('UPDATE employees SET name = ?, username = ?, password = ?, rol = ? WHERE id = ?', (name, username, password, rol, id_employee))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True
    
    def delete_employee(self, id_employee:int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM employees WHERE id = ?', (id_employee,))
        employee = cursor.fetchone()
        if not employee:
            return False
        cursor.execute('DELETE FROM employees WHERE id = ?', (id_employee,))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True