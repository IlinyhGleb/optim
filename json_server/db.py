import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
login TEXT PRIMARY KEY,
password TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS person (
id INT PRIMARY KEY,
name TEXT NOT NULL,
surname TEXT NOT NULL,
age INT NOT NULL,
height INT NOT NULL,
weight INT NOT NULL,
activity_level INT NOT NULL,
sex INT,
user_login TEXT,
FOREIGN KEY (user_login) REFERENCES User
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS refrigerator (
id INT PRIMARY KEY,
person_id INT,
FOREIGN KEY (person_id) REFERENCES person
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
id INT PRIMARY KEY,
name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS limits (
min INT,
max INT,
categories_id INT,
FOREIGN KEY (categories_id) REFERENCES categories
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
id INT PRIMARY KEY,
name TEXT,
caloricity INT,
categories_id INT,
FOREIGN KEY (categories_id) REFERENCES categories
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS refrigerator_has_product (
refrigerator_id INT,
product_id INT,
amount DOUBLE NOT NULL,
PRIMARY KEY(refrigerator_id,product_id),
FOREIGN KEY (product_id) REFERENCES product,
FOREIGN KEY (refrigerator_id) REFERENCES refrigerator
)
''')

cursor.execute('INSERT INTO User (login, password) VALUES (?, ?)', ('admin', '123'))
cursor.execute('INSERT INTO person (id, name, surname, age, height, weight, activity_level, sex, user_login) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (1, 'Мария', 'Лимонова', 21, 164, 48, 2, 0, 'admin'))
cursor.execute('INSERT INTO refrigerator (id, person_id) VALUES (?, ?)', (1, 1))

cursor.execute('INSERT INTO categories (id, name) VALUES (?, ?)', (1, 'Каши'))
cursor.execute('INSERT INTO categories (id, name) VALUES (?, ?)', (2, 'Крупы'))
cursor.execute('INSERT INTO categories (id, name) VALUES (?, ?)', (3, 'Мясо/рыба'))
cursor.execute('INSERT INTO categories (id, name) VALUES (?, ?)', (4, 'Фрукты'))
cursor.execute('INSERT INTO categories (id, name) VALUES (?, ?)', (5, 'Орехи'))
cursor.execute('INSERT INTO categories (id, name) VALUES (?, ?)', (6, 'Мучное'))
cursor.execute('INSERT INTO categories (id, name) VALUES (?, ?)', (7, 'Молочные продукты'))
cursor.execute('INSERT INTO categories (id, name) VALUES (?, ?)', (8, 'Овощи'))

cursor.execute('INSERT INTO limits (min, max, categories_id) VALUES (?, ?, ?)', (50, 200, 1))
cursor.execute('INSERT INTO limits (min, max, categories_id) VALUES (?, ?, ?)', (50, 200, 2))
cursor.execute('INSERT INTO limits (min, max, categories_id) VALUES (?, ?, ?)', (50, 300, 3))
cursor.execute('INSERT INTO limits (min, max, categories_id) VALUES (?, ?, ?)', (50, 200, 4))
cursor.execute('INSERT INTO limits (min, max, categories_id) VALUES (?, ?, ?)', (10, 30, 5))
cursor.execute('INSERT INTO limits (min, max, categories_id) VALUES (?, ?, ?)', (10, 30, 6))
cursor.execute('INSERT INTO limits (min, max, categories_id) VALUES (?, ?, ?)', (50, 200, 7))
cursor.execute('INSERT INTO limits (min, max, categories_id) VALUES (?, ?, ?)', (50, 150, 8))

cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (1, 'Овсянка', 68, 1))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (2, 'Греча', 343, 2))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (3, 'Рис', 360, 2))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (4, 'Курица вареная', 170, 3))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (5, 'Яблоко', 52, 4))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (6, 'Банан', 89, 4))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (7, 'Апельсин', 48, 4))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (8, 'Грецкий орех', 654, 5))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (9, 'Кешью', 553, 5))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (10, 'Бородинский хлеб', 259, 6))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (11, 'Хлебцы', 366, 6))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (12, 'Кефир', 40, 7))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (13, 'Творог', 159, 7))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (14, 'Огурец', 15, 8))
cursor.execute('INSERT INTO product (id, name, caloricity, categories_id) VALUES (?, ?, ?, ?)', (15, 'Помидор', 18, 8))

cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 1, 200))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 2, 300))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 3, 200))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 4, 500))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 5, 200))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 6, 200))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 7, 150))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 8, 40))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 9, 50))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 10, 300))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 11, 150))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 12, 1000))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 13, 500))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 14, 200))
cursor.execute('INSERT INTO refrigerator_has_product (refrigerator_id, product_id, amount) VALUES (?, ?, ?)', (1, 15, 200))

connection.commit()
connection.close()
