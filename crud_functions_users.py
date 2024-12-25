import sqlite3


connection_products = sqlite3.connect('products.db')
cursor_products = connection_products.cursor()

connection_users = sqlite3.connect('users.db')
cursor_users = connection_users.cursor()


def initiate_db_products():
    cursor_products.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    price INT
    )
    ''')


def initiate_db_users():
    cursor_users.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')


def add_products(product_id, title, description, price):
    cursor_products.execute(f'''
    INSERT INTO Products(id,title,description,price) VALUES('{product_id}','{title}','{description}','{price}')
    ''')
    connection_products.commit()


def add_user(username, email, age):
    check_users = cursor_users.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if not check_users.fetchall():
        cursor_users.execute('''
        INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)''', (username, email, age, 1000))
    connection_users.commit()


def is_in(username):
    user_exists = cursor_users.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
    return user_exists is not None


def get_all_products():
    cursor_products.execute('SELECT * FROM Products')
    products = cursor_products.fetchall()
    return products


if __name__ == '__main__':
    # initiate_db_products()
    # for i in range(1, 5):
    #     add_products(f'{i}', f'Продукт {i}', f'Описание {i}', f'{i * 100}')

    initiate_db_users()
    add_user('oleg', 'ex@gmail.com', 58)
    add_user('Nikita', 'ex@gmail.com', 20)
    print(is_in('oleg'))

    connection_products.close()
    connection_users.close()
