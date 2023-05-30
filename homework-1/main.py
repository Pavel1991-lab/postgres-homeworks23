"""Скрипт для заполнения данными таблиц в БД Postgres."""



import csv
import psycopg2

# Подключение к БД
conn = psycopg2.connect(
    host="5432",
    database="postgres",
    user="postgres",
    password="1938"
)
cursor = conn.cursor()


# Заполнение таблицы orders
with open('north_data/orders.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропуск заголовка
    for row in reader:
        cursor.execute(
            "INSERT INTO orders (customer_id, employee_id, order_date, ship_city) "
            "VALUES (%s, %s, %s, %s)",
            (row[1], row[2], row[3], row[4])
        )

# Заполнение таблицы customers
with open('north_data/customers.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропуск заголовка
    for row in reader:
        cursor.execute(
            "INSERT INTO customers (company_name, contact_name) "
            "VALUES (%s, %s)",
            (row[1], row[2])
        )

# Заполнение таблицы employees
with open('north_data/employees.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропуск заголовка
    for row in reader:
        cursor.execute(
            "INSERT INTO employees (first_name, last_name, title, birth_date, notes) "
            "VALUES (%s, %s, %s, %s, %s)",
            (row[2], row[1], row[3], row[4], row[14])
        )

# Заполнение таблицы shippers
with open('north_data/shippers.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропуск заголовка
    for row in reader:
        cursor.execute(
            "INSERT INTO shippers (company_name, phone) "
            "VALUES (%s, %s)",
            (row[1], row[2])
        )

# Сохранение изменений и закрытие соединения
conn.commit()
cursor.close()
conn.close()

