#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Использование функций в качестве переменных
# Документирование функций
#


def my_add(a, b):
    """Сложенин двух чисел"""  # это документирование функции
    print('Функция my_add')
    return a + b


def my_mult(a, b):
    """Умножение двух чисел"""
    print('Функция my_mult')
    return a * b


def my_max(a, b):
    """Большее из двух чисел"""
    print('Функция my_max')
    if a > b:
        return a
    else:
        return b


def my_min(a, b):
    """Меньшее из двух чисел"""
    print('Функция my_min')
    if a < b:
        return a
    else:
        return b


# Вывод документирования функций
# Использование функций в качестве переменных

print('\nИспользование функций в качестве переменных:')
print('-' * 46)
print('1. Функция my_add\t:' + my_add.__doc__)
print('2. Функция my_mult\t:' + my_mult.__doc__)
print('3. Функция my_max\t:' + my_max.__doc__)
print('4. Функция my_min\t:' + my_min.__doc__)
print('-' * 46)
nom_func = int(input('Введите номер функции\t: '))

if nom_func == 1:
    run = my_add
elif nom_func == 2:
    run = my_mult
elif nom_func == 3:
    run = my_max
elif nom_func == 4:
    run = my_min
else:
    print('Ошибка! Не верно введен номер функции!')

if run != 0:
    a = float(input('Введите число А\t\t: '))
    b = float(input('Введите число B\t\t: '))
    print('-' * 46)
    result = run(a, b)
    print('Результат = ' + str(result))
