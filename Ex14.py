#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Выход из цикла. break и continue
#

# Оператор break    - осуществляет выход из цикла.
# Оператор continue - выполняет переход к следующей итерации цикла.

# Программа Обменный пункт

print("Для выхода нажмите Y")

while True:
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y":
        break       # выход из цикла
    money = int(data)
    if money < 0:
        print("Сумма должна быть положительной!")
        continue    # переход к следующей итерации
    cache = round(money / 56, 2)
    print("К выдаче", cache, "долларов")

print("Работа обменного пункта завершена")
