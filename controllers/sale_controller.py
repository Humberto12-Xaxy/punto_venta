from database.database_connection import DatabaseConnection
from models.sale import Sale, DataSale


class SaleController:
    def __init__(self):
        self._db = DatabaseConnection().connection("db.sqlite3")

    def get_all_sales(self):
        with self._db as db:
            cursor =db.cursor()
            cursor.execute(
                '''
                SELECT sales.id, sales.date_sale, sales.total, employees.name FROM sales
                INNER JOIN employees ON sales.id_employee = employees.id
                '''
            )
            sales = cursor.fetchall()
            sales = [DataSale(*sale) for sale in sales]
            cursor.close()
            return sales

    def get_sale_by_id(self, id_sale: int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM sales WHERE id = ?', (id_sale,))
        sale = cursor.fetchone()
        cursor.close()
        self._db.close()
        return Sale(*sale)

    def add_sale(self, date: str, total: int, id_employee: int) -> int:
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO sales VALUES (?,?,?,?)',
                        (None, date, total, id_employee))
            id_sale = cursor.lastrowid
            db.commit()
            cursor.close()
            return id_sale

    def update_sale(self, id_sale: int, id_employee: int, id_product: int, quantity: int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM sales WHERE id = ?', (id_sale,))
        sale = cursor.fetchone()
        if not sale:
            return False
        cursor.execute('UPDATE sales SET id_employee = ?, id_product = ?, quantity = ? WHERE id = ?',
                    (id_employee, id_product, quantity, id_sale))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True

    def delete_sale(self, id_sale: int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM sales WHERE id = ?', (id_sale,))
        sale = cursor.fetchone()
        if not sale:
            return False
        cursor.execute('DELETE FROM sales WHERE id = ?', (id_sale,))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True

    def get_sales_by_id_employee(self, id_employee: int):
        cursor = self._db.cursor()
        cursor.execute(
            'SELECT * FROM sales WHERE id_employee = ?', (id_employee,))
        sales = cursor.fetchall()
        sales = [Sale(*sale) for sale in sales]
        cursor.close()
        self._db.close()
        return sales

    def get_sales_by_id_product(self, id_product: int):
        cursor = self._db.cursor()
        cursor.execute(
            'SELECT * FROM sales WHERE id_product = ?', (id_product,))
        sales = cursor.fetchall()
        sales = [Sale(*sale) for sale in sales]
        cursor.close()
        self._db.close()
        return sales

    def update_sale_quantity(self, id_sale: int, quantity: int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM sales WHERE id = ?', (id_sale,))
        sale = cursor.fetchone()
        if not sale:
            return False
        cursor.execute(
            'UPDATE sales SET quantity = ? WHERE id = ?', (quantity, id_sale))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True

    def update_sale_by_employee_and_product(self, id_employee: int, id_product: int, quantity: int):
        cursor = self._db.cursor()
        cursor.execute(
            'SELECT * FROM sales WHERE id_employee = ? AND id_product = ?', (id_employee, id_product))
        sale = cursor.fetchone()
        if not sale:
            return False
        cursor.execute('UPDATE sales SET quantity = ? WHERE id_employee = ? AND id_product = ?',
                    (quantity, id_employee, id_product))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True
