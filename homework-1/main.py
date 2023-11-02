"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def read_filedata(filepath: str) -> list:
    """Считывание данных из таблицы и возвращение списка кортежей"""
    with open(filepath, encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=",")
        data = []
        for row in file_reader:
            data.append(tuple(row))
    data.pop(0)
    return data


# Заполнить данными:
customers_data = read_filedata('north_data/customers_data.csv')
employees_data = read_filedata('north_data/employees_data.csv')
orders_data = read_filedata('north_data/orders_data.csv')

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='qwerty')
try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany(f"INSERT INTO customers VALUES (%s, %s, %s)", customers_data)
            cur.executemany(f"INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)", employees_data)
            cur.executemany(f"INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", orders_data)
            conn.commit()
finally:
    conn.close()
import psycopg2
import csv


def read_filedata(filepath: str) -> list:
    """Считывание данных из таблицы и возвращение списка кортежей"""
    with open(filepath, encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=",")
        data = []
        for row in file_reader:
            data.append(tuple(row))
    data.pop(0)
    return data


# Заполнить данными:
customers_data = read_filedata('north_data/customers_data.csv')
employees_data = read_filedata('north_data/employees_data.csv')
orders_data = read_filedata('north_data/orders_data.csv')

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='qwerty')
try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany(f"INSERT INTO customers VALUES (%s, %s, %s)", customers_data)
            cur.executemany(f"INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)", employees_data)
            cur.executemany(f"INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)", orders_data)
            conn.commit()
finally:
    conn.close()
