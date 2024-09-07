import sqlite3

conn = sqlite3.connect('db.sqlite3')

def create_table():
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            code TEXT UNIQUE
        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT UNIQUE,
            password TEXT NOT NULL,
            rol TEXT CHECK(rol IN ('admin', 'cajero')) NOT NULL
        )
        '''
    )

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_sale DATETIME DEFAULT CURRENT_TIMESTAMP,
        total REAL NOT NULL,
        id_employee INTEGER NOT NULL,
        FOREIGN KEY (id_employee) REFERENCES employees(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS details_sale (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_sale INTEGER NOT NULL,
        id_product INTEGER NOT NULL,
        count INTEGER NOT NULL,
        unitario_price REAL NOT NULL,
        subtotal REAL NOT NULL,
        FOREIGN KEY (id_sale) REFERENCES sales(id),
        FOREIGN KEY (id_product) REFERENCES products(id)
    )
    ''')

    conn.commit()
    conn.close()

    print('database created')