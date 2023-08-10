"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

EMPLOYEES_DATA = os.path.join('north_data', 'employees_data.csv')
CUSTOMERS_DATA = os.path.join('north_data', 'customers_data.csv')
ORDERS_DATA = os.path.join('north_data', 'orders_data.csv')

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="54321")
try:
    with conn:
        with conn.cursor() as cur:
            with open(EMPLOYEES_DATA) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                (row['employee_id'],
                                 row['first_name'],
                                 row['last_name'],
                                 row['title'],
                                 row['birth_date'],
                                 row['notes']
                                 ))
            with open(CUSTOMERS_DATA) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                (row['customer_id'],
                                 row['company_name'],
                                 row['contact_name']
                                 ))
            with open(ORDERS_DATA) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                (row['order_id'],
                                 row['customer_id'],
                                 row['employee_id'],
                                 row['order_date'],
                                 row['ship_city']
                                 ))
finally:
    conn.close()
