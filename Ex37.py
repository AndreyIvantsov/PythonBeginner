#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Бинарные файлы: Модуль shelve
#

# Для работы с бинарными файлами в Python может применяться еще один
# модуль - shelve. Он сохраняет объекты в файл с определенным ключом.
# Затем по этому ключу может извлечь ранее сохраненный объект из
# файла. Процесс работы с данными через модуль shelve напоминает
# работу со словарями, которые также используют ключи для сохранения
# и извлечения объектов.

# Для открытия файла модуль shelve использует функцию open():
# open(путь_к_файлу[, flag="c"[, protocol=None[, writeback=False]]])

# Где параметр flag может принимать значения:
#
#   c   : файл открывается для чтения и записи (значение по
#         умолчанию). Если файл не существует, то он создается.
#
#   r   : файл открывается только для чтения.
#
#   w   : файл открывается для записи.
#
#   n   : файл открывается для записи Если файл не существует, то он
#         создается. Если он существует, то он перезаписывается

# Для закрытия подключения к файлу вызывается метод close()

import shelve

FILENAME = "states2.dat"
d = shelve.open(FILENAME)
d.close()

# Либо можно открывать файл с помощью оператора with. Сохраним и
# считаем в файл несколько объектов:

# Запись данных предполагает установку значения для определенного
# ключа:

FILENAME = "states2.dat"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Madrid"])

# При чтении данных, если запрашиваемый ключ отсутствует, то
# генерируется исключение. В этом случае перед получением мы можем
# проверять на наличие ключа с помощью оператора in:

with shelve.open(FILENAME) as states:
    key = "Brussels"
    if key in states:
        print(states[key])

# Также мы можем использовать метод get(). Первый параметр
# метода - ключ, по которому следует получить значение,
# а второй - значение по умолчанию, которое возвращается,
# если ключ не найден.

with shelve.open(FILENAME) as states:
    state = states.get("Brussels", "Undefined")
    print(state)

# Используя цикл for, можно перебрать все значения из файла:

with shelve.open(FILENAME) as states:
    for key in states:
        print(key, "\t - ", states[key])

# Метод keys() возвращает все ключи из файла, а метод
# values() - все значения:

with shelve.open(FILENAME) as states:
    for city in states.keys():
        print(city, end=" ")     # London Paris Berlin Madrid
    print()
    for country in states.values():
        print(country, end=" ")  # Great Britain France Germany Spain

# Еще один метод items() возвращает набор кортежей. Каждый кортеж
# содержит ключ и значение.

with shelve.open(FILENAME) as states:
    for state in states.items():
        print(state)

# Обновление данных

# Для изменения данных достаточно присвоить по ключу новое значение,
# а для добавления данных - определить новый ключ:


FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:

    states["London"] = "United Kingdom"
    states["Brussels"] = "Belgium"
    for key in states:
        print(key, " - ", states[key])

# Удаление данных

# Для удаления с одновременным получением можно использовать функцию
# pop(), в которую передается ключ элемента и значение по умолчанию,
#  если ключ не найден:

with shelve.open(FILENAME) as states:
    state = states.pop("London", "NotFound")
    print(state)

# Также для удаления может применяться оператор del:

with shelve.open(FILENAME) as states:
    del states["Madrid"]    # удаляем объект с ключом Madrid

# Для удаления всех элементов можно использовать метод clear():

with shelve.open(FILENAME) as states:
    states.clear()
