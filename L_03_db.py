import sqlite3

connection = sqlite3.connect('l_03_db.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
first_name TEXT NOT NULL,
block INT
)
''')


def add_user(user_id, username, first_name):
    check_users = cursor.execute('SELECT * FROM Users WHERE id = ?', (user_id,))  # вернется или пусто или user_id
    if not check_users.fetchall():  # Если список пустой, значит пользователь не существует
        cursor.execute(f'''
        INSERT INTO Users(id,username,first_name,block) VALUES('{user_id}','{username}','{first_name}',0)
        ''')
    connection.commit()


def show_all_users():
    user_list = cursor.execute('SELECT * FROM Users')
    message = ''
    for user in user_list:
        message += f'{user[0]} @{user[1]} {user[2]} {user[3]}\n'
    # connection.commit() - Не нужно вызывать commit здесь, так как мы только читаем данные
    return message


def show_stat():
    count_users = cursor.execute('SELECT COUNT(*) FROM Users').fetchone()
    return count_users[0]


def user_block(user_id):
    cursor.execute('UPDATE Users SET block = ? WHERE id = ?', (1, user_id))
    connection.commit()


def user_unblock(user_id):
    cursor.execute('UPDATE Users SET block = ? WHERE id = ?', (0, user_id))
    connection.commit()


def check_block(user_id):
    cursor.execute('SELECT username, block FROM Users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    return f'{user[0]} {user[1]}' if user else None

def check_block_(user_id):
    user = cursor.execute(f'SELECT username, block FROM Users WHERE id = {user_id}').fetchone()
    return f'{user[0]} {user[1]}' if user else None


def check_block__(user_id):
    user = cursor.execute(f'SELECT username, block FROM Users WHERE id = {user_id}').fetchone()
    return user if user else None


if __name__ == '__main__':
    add_user(1, 'ok', 'oleg')
    print(show_all_users())  # Показываем всех пользователей
    print(show_stat())
    # user_block(1)
    user_unblock(1)
    print(check_block(1))
    print(check_block_(1))
    print(check_block__(1))
    connection.close()
