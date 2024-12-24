import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    price INT
    )
    ''')


def add_products(product_id, title, description, price):
    cursor.execute(f'''
    INSERT INTO Products(id,title,description,price) VALUES('{product_id}','{title}','{description}','{price}')
    ''')
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products

if __name__ == '__main__':
    initiate_db()
    for i in range(1, 5):
        add_products(f'{i}', f'Продукт {i}', f'Описание {i}', f'{i * 100}')

    connection.close()
