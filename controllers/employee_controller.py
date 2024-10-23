from database.database_connection import DatabaseConnection
from models.employee import Employee

class EmployeeController:
    def __init__(self):
        self._db = DatabaseConnection().connection("db.sqlite3")
    
    def get_all_employees(self):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM employees ORDER BY name ASC')
            employees = cursor.fetchall()
            employees = [Employee(*employee) for employee in employees]
            cursor.close()
            return employees
        
    def get_employees_by_name(self, name:str):
        with self._db as db:
            cursor = db.cursor()
            name = '%' + name + '%'
            cursor.execute('SELECT * FROM employees WHERE LOWER(name) LIKE ? ORDER BY name ASC', (name.lower(),))
            employees = cursor.fetchall()
            cursor.close()
            return [Employee(*employee) for employee in employees]

    
    def get_employee_by_username(self, username:str):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT password FROM employees WHERE username = ?', (username,))
            password = cursor.fetchone()
            cursor.close()
            return password
        
    def login_employee(self, username:str, password:str):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM employees WHERE username = ? AND password = ?', (username, password))
            employee = cursor.fetchone()
            cursor.close()
            return Employee(*employee)
        
    def get_employee_by_id(self, id_employee:int):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM employees WHERE id = ?', (id_employee,))
            employee = cursor.fetchone()
            cursor.close()
            return Employee(*employee)

    def add_employee(self, name:str, username:str, password:str, rol:str):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO employees VALUES (?,?,?,?,?)', (None, name, username, password, rol))
            self._db.commit()
            cursor.close()
            return True

    def update_employee(self, id_employee:int, name:str, username:str, password:str, rol:str):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM employees WHERE id = ?', (id_employee,))
            employee = cursor.fetchone()
            if not employee:
                return False
            cursor.execute('UPDATE employees SET name = ?, username = ?, password = ?, rol = ? WHERE id = ?', (name, username, password, rol, id_employee))
            self._db.commit()
            cursor.close()
            return True
    
    def delete_employee(self, id_employee:int):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM employees WHERE id = ?', (id_employee,))
            employee = cursor.fetchone()
            if not employee:
                return False
            cursor.execute('DELETE FROM employees WHERE id = ?', (id_employee,))
            self._db.commit()
            cursor.close()
            return True