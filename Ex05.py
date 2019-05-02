# -*- coding: utf-8 -*-

#
# Функции преобразования чисел
#

# Ряд встроенных функций в Python позволяют работать с числами. 
# В частности, функции int() и float() позволяют привести 
# значение к типу int и float соответственно.

first_number = "2"
second_number = 3
third_number = int(first_number) + second_number
print(third_number) # 5

first_number = 2.0001
second_number = 5
third_number = first_number / second_number
print(third_number) # 0.40002000000000004

# для округления результата мы можем использовать функцию round():
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(third_number)  # 2.1001
print(round(third_number, 2))  # 2.1001
