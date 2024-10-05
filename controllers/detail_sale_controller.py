from database.database_connection import DatabaseConnection
from models.detail_sale import DetailSale, DetailSaleById


class DetailSaleController:
    def __init__(self):
        self._db = DatabaseConnection().connection("db.sqlite3")

    def get_all_detail_sales(self):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM detail_sales')
        detail_sales = cursor.fetchall()
        detail_sales = [DetailSale(*detail_sale)
                        for detail_sale in detail_sales]
        cursor.close()
        self._db.close()
        return detail_sales

    def get_detail_sale_by_id(self, id_detail_sale: int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM detail_sales WHERE id = ?',
                       (id_detail_sale,))
        detail_sale = cursor.fetchone()
        cursor.close()
        self._db.close()
        return DetailSale(*detail_sale)

    def add_detail_sale(self, id_sale: int, id_product: int, quantity: int, price: float, subtotal: float):
        with self._db as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO details_sale VALUES (?,?,?,?,?,?)',
                           (None, id_sale, id_product, quantity, price, subtotal))
            db.commit()
            cursor.close()
            return True

    def update_detail_sale(self, id_detail_sale: int, id_sale: int, id_product: int, quantity: int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM detail_sales WHERE id = ?',
                       (id_detail_sale,))
        detail_sale = cursor.fetchone()
        if not detail_sale:
            return False
        cursor.execute('UPDATE detail_sales SET id_sale = ?, id_product = ?, quantity = ? WHERE id = ?',
                       (id_sale, id_product, quantity, id_detail_sale))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True

    def delete_detail_sale(self, id_detail_sale: int):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM detail_sales WHERE id = ?',
                       (id_detail_sale,))
        detail_sale = cursor.fetchone()
        if not detail_sale:
            return False
        cursor.execute('DELETE FROM detail_sales WHERE id = ?',
                       (id_detail_sale,))
        self._db.commit()
        cursor.close()
        self._db.close()
        return True

    def get_detail_sale_by_id_sale(self, id_sale: int):
        sql = '''
        SELECT details_sale.id, details_sale.count, products.name, products.price, details_sale.subtotal
        FROM details_sale
        INNER JOIN products ON details_sale.id_product = products.id
        WHERE details_sale.id_sale = ?
        '''
        with self._db as db:
            cursor = db.cursor()
            cursor.execute(
                sql, (id_sale,))
            detail_sales = cursor.fetchall()
            detail_sales = [DetailSaleById(*detail_sale)
                            for detail_sale in detail_sales]
            cursor.close()
            return detail_sales
