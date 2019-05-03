#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Обработка исключений
#

# При возникновении исключения работа программы прерывается,
# и чтобы избежать подобного поведения и обрабатывать исключения
# в Python есть конструкция try..except, которая имеет следующее
# формальное определение:

# try:
#     инструкции
# except [Тип_исключения]:
#     инструкции

try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except Exception:
    print("Общее исключение")
print("Завершение программы")

# Тип Exception представляет общее исключение, под которое попадают
# все исключительные ситуации. Поэтому в данном случае любое
# исключение, которое не представляет тип ValueError или
# ZeroDivisionError, будет обработано в блоке except Exception.