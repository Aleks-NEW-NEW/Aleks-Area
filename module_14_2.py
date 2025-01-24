import sqlite3


connection = sqlite3.connect('not_telegram_m14_2.db')
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")


cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')


# for n in range(1, 11):
#     cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
#                    (f'User{n}', f'example{n}@gmail.com', n * 10, 1000)
#                    )
#
#
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance=? WHERE username=?', (500, f'User{i}'))
#
#
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username=?', (f'User{i}', ))
#
#
# cursor.execute('SELECT * FROM Users WHERE age != ?', (60, ))
#
# users_age = cursor.fetchall()
#
# for user in users_age:
#     print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')


cursor.execute('DELETE FROM Users WHERE id=?', (6, ))


cursor.execute('SELECT COUNT(*) FROM Users')

total_users = cursor.fetchone()[0]


cursor.execute('SELECT SUM(balance) FROM Users')

total_balance = cursor.fetchone()[0]

print(total_balance / total_users)


connection.commit()
connection.close()
