#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Возвращение результата функцией
#

# Функция может возвращать результат. Для этого в функции
# используется оператор return, после которого указывается
# возвращаемое значение:


def exchange(usd_rate, money):
    result = round(money/usd_rate, 2)
    return result


result1 = exchange(60, 30000)
print(result1)
result2 = exchange(56, 30000)
print(result2)
result3 = exchange(65, 30000)
print(result3)

# В Python функция может возвращать сразу несколько значений:


def create_default_user():
    name = "Tom"
    age = 33
    return name, age


user_name, user_age = create_default_user()
print("Name:", user_name, "\t Age:", user_age)

# Здесь функция create_default_user возвращает два значения: name и age.
# При вызове функции эти значения по порядку присваиваются переменным
# user_name и user_age, и мы их можем использовать.
