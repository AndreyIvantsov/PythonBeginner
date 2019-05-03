#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Файлы CSV: работа со словарями
#

# Модуль csv имеет специальные дополнительные возможности для работы
# со словарями. В частности, функция csv.DictWriter() возвращает
# объект writer, который позволяет записывать в файл. А функция
# csv.DictReader() возвращает объект reader для чтения из файла.

import csv

FILENAME = "users.csv"

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    # запись нескольких строк
    writer.writerows(users)

    user = {"name": "Sam", "age": 41}
    # запись одной строки
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "\t - ", row["age"])

# Запись строк также производится с помощью методов writerow() и
# writerows(). Но теперь каждая строка представляет собой отдельный
# словарь, и кроме того, производится запись и заголовков столбцов
# с помощью метода writeheader(), а в метод csv.DictWriter в
# качестве второго параметра передается набор столбцов.

# При чтении строк, используя названия столбцов, мы можем обратиться
# к отдельным значениям внутри строки: row["name"].
