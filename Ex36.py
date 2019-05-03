#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Бинарные файлы: Модуль pickle
#

# Бинарные файлы в отличие от текстовых хранят информацию в виде
# набора байт. Для работы с ними в Python необходим встроенный модуль
# pickle. Этот модуль предоставляет два метода:
#
#   dump(obj, file) : записывает объект obj в бинарный файл file
#   load(file)      : считывает данные из бинарного файла в объект

# При открытии бинарного файла на чтение или запись также надо
# учитывать, что нам нужно применять режим "b" в дополнение к режиму
# записи ("w") или чтения ("r").

# Допустим, надо надо сохранить два объекта:

import pickle

FILENAME = "user.dat"

name = "Tom"
age = 19

with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)

# С помощью функции dump последовательно записываются два объекта.
# Поэтому при чтении файла также последовательно посредством функции
# load мы можем считать эти объекты.

# Подобным образом мы можем сохранять и извлекать из файла наборы
# объектов:


FILENAME = "users.dat"

users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]

with open(FILENAME, "wb") as file:
    pickle.dump(users, file)


with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:",
              user[1], "\tЖенат(замужем):", user[2])

# В зависимости от того, какой объект мы записывали функцией dump,
# тот же объект будет возвращен функцией load при считывании файла.
