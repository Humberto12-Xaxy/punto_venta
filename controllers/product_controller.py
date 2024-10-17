from database.database_connection import DatabaseConnection
from models.product import Product


class ProductController:
    def __init__(self):
        self._db = DatabaseConnection().connection("db.sqlite3")
    
    def get_all_products(self):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM products ORDER BY name ASC')
            products = cursor.fetchall()
            products = [Product(*product) for product in products]
            cursor.close()
            return products
        
    def get_product_by_code(self, code:str):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM products WHERE code = ?', (code,))
            product = cursor.fetchone()
            if not product:
                return None
            cursor.close()
            return Product(*product)
    
    def get_products_by_name(self, name:str):
        with self._db as db:
            cursor = db.cursor()
            name = '%' + name + '%'
            cursor.execute('SELECT * FROM products WHERE LOWER(name) LIKE ? ORDER BY name ASC', (name.lower(),))
            products = cursor.fetchall()
            cursor.close()
            return [Product(*product) for product in products]

    def add_product(self, name:str, price:float, stock:int, code:str):
        try:
            with self._db as db:
                cursor = db.cursor()
                cursor.execute('INSERT INTO products VALUES (?,?,?,?,?)', (None, name, price, stock, code))
                self._db.commit()
                cursor.close()    
                return True
        except Exception as e:
            print(e)
            return False
    
    def get_product_by_id(self, id_product:int):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM products WHERE id = ?', (id_product,))
            product = cursor.fetchone()
            cursor.close()
            return Product(*product)
        
    def update_product(self, id_product:int, name:str, price:float, stock:int, code:str):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM products WHERE id = ?', (id_product,))
            product = cursor.fetchone()
            if not product:
                return False
            cursor.execute('UPDATE products SET name = ?, price = ?, stock = ?, code = ? WHERE id = ?', (name, price, stock, code, id_product))
            db.commit()
            cursor.close()
            return True

    def update_stock(self, id_product:int, stock:int):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM products WHERE id = ?', (id_product,))
            product = cursor.fetchone()
            if not product:
                return False
            cursor.execute('UPDATE products SET stock = ? WHERE id = ?', (stock, id_product))
            db.commit()
            cursor.close()
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
    


if __name__ == "__main__":
    print(ProductController().get_all_products())