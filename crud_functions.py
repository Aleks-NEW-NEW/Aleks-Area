import sqlite3


connection = sqlite3.connect('telegram_m14_4.db')
cursor = connection.cursor()


products_names = ['Батончик', 'Протеин', 'Креатин', 'BCAA']


def initiate_db():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)

    # Заполним таблицу продуктами. Если еще не заполнена.
    products_count = cursor.execute('SELECT COUNT(*) FROM Products')

    if not products_count.fetchone()[0]:
        for i, name in enumerate(products_names, start=1):
            cursor.execute(
                f'INSERT INTO Products(title, description, price) VALUES(?, ?, ?)',
                (name, f'Описание {i}', i * 100)
            )

    connection.commit()


initiate_db()


def get_all_products():

    all_products = cursor.execute('SELECT * FROM Products').fetchall()

    return all_products


connection.commit()

# Закомментирую строчку закрытия БД.
# Если оставить закрытой БД, то при запуска основного файла "module_14_4.py" телеграм-бота возникнет ошибка:
# "sqlite3.ProgrammingError: Cannot operate on a closed database."

# connection.close()
