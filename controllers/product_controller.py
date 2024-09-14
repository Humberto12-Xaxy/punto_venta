from database.database_connection import DatabaseConnection
from models.product import Product


class ProductController:
    def __init__(self):
        self._db = DatabaseConnection().connection("db.sqlite3")
    
    def get_all_products(self):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        products = [Product(*product) for product in products]
        cursor.close()
        self._db.close()
        return products
    
    def get_product_by_code(self, code:str):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM products WHERE code = ?', (code,))
        product = cursor.fetchone()
        cursor.close()
        self._db.close()
        return Product(*product)

    def add_product(self, name:str, price:float, stock:int, code:str):
        cursor = self._db.cursor()
        cursor.execute('INSERT INTO products VALUES (?,?,?,?,?)', (None, name, price, stock, code))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True
    
    def update_product(self, id_product:int, name:str, price:float, stock:int, code:str):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM products WHERE id = ?', (id_product,))
        product = cursor.fetchone()
        if not product:
            return False
        cursor.execute('UPDATE products SET name = ?, price = ?, stock = ?, code = ? WHERE id = ?', (name, price, stock, code, id_product))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True
    
    def delete_product(self, id_product:int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM products WHERE id = ?', (id_product,))
        product = cursor.fetchone()
        if not product:
            return False
        cursor.execute('DELETE FROM products WHERE id = ?', (id_product,))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True
    
