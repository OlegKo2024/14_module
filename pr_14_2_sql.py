import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
Id INTEGER PRIMARY KEY,
Username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# for i in range(1, 11):
#     cursor.execute(
#         'INSERT INTO Users(username,email,age,balance) VALUES (?,?,?,?)',
#         (f'user{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'),
#     )

# cursor.execute('UPDATE Users SET balance = ? WHERE Id % 2 != 0', (500,))

# cursor.execute('DELETE FROM Users WHERE Id % 3 = ?', (1,))

# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

cursor.execute('DELETE FROM Users WHERE id = ?', ('6',))

cursor.execute('SELECT COUNT(*) FROM Users')
result_count_all = cursor.fetchone()[0]
# print(result_count_all) # 5

cursor.execute('SELECT SUM(balance) FROM Users')
result_sum_all = cursor.fetchone()[0]
# print(result_sum_all)   # 3500

cursor.execute('SELECT AVG(balance) FROM Users')
result_avg_all = cursor.fetchone()[0]
# print(result_avg_all)

print(result_sum_all / result_count_all)

connection.commit()
connection.close()
