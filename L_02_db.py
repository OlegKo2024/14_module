import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('SELECT COUNT(*) FROM Users')
result_count_all = cursor.fetchone()[0]     # Метод fetchone() возвращает эту строку в виде кортежа (tuple) или списка (зависит от настроек библиотеки)
                                            # [0] - это обращение к элементу кортежа по индексу - получаем количество записей.
print(result_count_all)

cursor.execute('SELECT COUNT(*) FROM Users WHERE age > ?', ('30',))
result_count_some = cursor.fetchone()[0]
print(result_count_some)

cursor.execute('SELECT username, age FROM Users WHERE age > ?', (58,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Возраст: {user[1]}')

cursor.execute('SELECT SUM(age) FROM Users')
result_sum_all = cursor.fetchone()[0]
print(result_sum_all)

cursor.execute('SELECT SUM(age) FROM Users WHERE age > ?', ('58',))
result_sum_some = cursor.fetchone()[0]
print(result_sum_some)

print(result_sum_all / result_count_all)

cursor.execute('SELECT AVG(age) from Users')
result_average = cursor.fetchone()[0]
print(int(result_average))

cursor.execute('SELECT MIN(age) from Users')
result_min = cursor.fetchone()[0]
print(int(result_min))

cursor.execute('SELECT MAX(age) from Users')
result_max = cursor.fetchone()[0]
print(int(result_max))

cursor.execute('SELECT username, age FROM Users WHERE age = ?', (result_max,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Возраст: {user[1]}')

cursor.execute('SELECT username, age FROM Users WHERE age = ?', (result_min,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Возраст: {user[1]}')

connection.commit()
connection.close()
