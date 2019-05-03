#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Параметры функций
#

# Значения по умолчанию


def say_hello(name="Tom"):
    print("Hello,", name)


say_hello()
say_hello("Bob")

# Именованные параметры


def display_info(name, age):
    print("Name:", name, "\t", "Age:", age)


display_info(age=22, name="Tom")

# Неопределенное количество параметров


def sum(*params):
    result = 0
    for n in params:
        result += n
    return result


sumOfNumbers1 = sum(1, 2, 3, 4, 5)      # 15
sumOfNumbers2 = sum(3, 4, 5, 6)         # 18
print(sumOfNumbers1)
print(sumOfNumbers2)
