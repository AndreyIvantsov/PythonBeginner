# -*- coding: utf-8 -*-

#
# Типы данных
#

'''
В Python существует множество различных типов данных, которые подразделяются на категории: 
числа, последовательности, словари, наборы:

    boolean     - логическое значение True или False
    int         - представляет целое число, для хранения которого использует 4 байта в памяти компьютера.
    float       - представляет число с плавающей точкой, для хранения которого используется 8 байт, 
                  например, 1.2 или 34.76
    complex     - комплексные числа
    str         - строки, например "hello". В Python 3.x строки представляют набор символов в кодировке Unicode
    bytes       - последовательность чисел в диапазоне 0-255
    byte array  - массив байтов, аналогичен bytes с тем отличием, что может изменяться
    list        - список
    tuple       - кортеж
    set         - неупорядоченная коллекция уникальных объектов
    frozen set  - то же самое, что и set, только не может изменяться (immutable)
    dict    -   ш словарь, где каждый элемент имеет ключ и значение

Python является языком с динамической типизацией. Он определяет тип данных переменной исходя из значения, 
которое ей присвоено.
'''

x = 3.9e3
print(x)  # 3900.0
 
x = 3.9e-3
print(x)  # 0.0039

user_id = "12tomsmith438"  # тип str
print(user_id)
 
user_id = 234  # тип int
print(user_id)

# С помощью функции type() динамически можно узнать текущий тип переменной:
	
user_id = "12tomsmith438"
print(type(user_id))  # <class 'str'>
 
user_id = 234
print(type(user_id))  # <class 'int'>