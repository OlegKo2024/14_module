import sqlite3

# import sqlite3: Здесь происходит импорт модуля sqlite3, который позволяет взаимодействовать с базой данных SQLite.
# Этот модуль предоставляет функции для создания, чтения, обновления и удаления данных в реляционных базах данных

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
# connection = ...: Здесь мы создаем подключение к базе данных, которая называется database.db. Если файл не существует,
# он будет создан автоматически. Переменная connection хранит это подключение, позволяя взаимодействовать с базой данных
# cursor = ...: Создаем объект cursor, который позволяет выполнять SQL-ЗАПРОСЫ к базе данных, связанной с
# с нашим подключением. Этот объект используется для отправки команд SQLite и получения данных.

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
Id INTEGER PRIMARY KEY,
Username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')
# cursor.execute('''...''' ): Внутри этого блока мы выполняем команду SQL. В данном случае, это команда для создания
# таблицы Users, если она еще не существует. Внутри команды:

# Однако, если ваш запрос длинный и требует форматирования (например, много строк или сложная структура), использование
# тройных кавычек (''' ''') удобно, так как это позволяет вам разбить код по строкам, улучшая читаемость.
# Вот почему чаще используются тройные кавычки для многострочных SQL-запросов в коде. Суть в том, что в Python вы
# можете использовать оба варианта, но тройные кавычки удобнее для сложных запросов.

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)'): Здесь создается индекс с именем idx_email
# для столбца email в таблице Users, если он еще не существует. Индексы ускоряют поиск данных при использовании условий
# поиска, связанных с полем email.

# ДОБАВЛЯТЬ ОБНОВЛЯТЬ УДАЛЯТЬ ДАННЫЕ:
# ДОБАВЛЯТЬ
# cursor.execute('INSERT INTO Users(username,email,age) VALUES (?,?,?)', ('kob', 'ex.mail.ru', '20'))
# for i in range(30):
#     cursor.execute(
#         'INSERT INTO Users(username,email,age) VALUES (?,?,?)',
#         (f'newuser{i}', f'{i}ex.gmail.com', f'{30 + i}')
# #     )

# # ОБНОВЛЯТЬ
# cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))

# # УДАЛЯТЬ
# cursor.execute('DELETE FROM Users WHERE age = ?', ('29',))

# READ
# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()
# for user in users:
#     print(user)

# SELECT
# cursor.execute('SELECT username, age FROM Users WHERE age > ?', (49,))
# users = cursor.fetchall()
# for user in users:
#     print(user)

# GROUP
cursor.execute('SELECT username, email, age FROM Users GROUP BY age')   # сортировка по age и плюс убрались повторения
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()
# connection.commit(): Эта команда сохраняет все изменения, внесенные в базу данных с момента последнего коммита.
# Без нее изменения будут потеряны, поэтому необходимо ее вызывать после выполнения модифицирующих действий.
# connection.close(): В последней строке мы закрываем подключение к базе данных, освобождая все ресурсы, связанные
# с этим подключением. Это хорошая практика завершать соединение с базой данных, когда оно больше не нужно.
# Таким образом, приведенный код создает базу данных с таблицей пользователей и индексом для поля электронной
# почты, что улучшает производительность запросов.
