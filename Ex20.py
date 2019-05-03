#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Область видимости переменных
#

# В Python есть два типа контекста: глобальный и локальный.

# Глобальный контекст подразумевает, что переменная является
# глобальной, она определена вне любой из функций и доступна
# любой функции в программе.

name = "Tom"


def say_hi():
    print("Hello", name)


def say_bye():
    print("Good bye", name)


say_hi()
say_bye()


# Локальная переменная определяется внутри функции и доступна
# только из этой функции, то есть имеет локальную область
# видимости:

def say_hi():
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)


def say_bye():
    name = "Tom"
    print("Good bye", name)


say_hi()
say_bye()

# Есть еще один вариант определения переменной, когда локальная
# переменная скрывают глобальную с тем же именем:

name = "Tom"


def say_hi():
    print("Hello", name)


def say_bye():
    name = "Bob"
    print("Good bye", name)


say_hi()  # Hello Tom
say_bye()  # Good bye Bob


# Если же мы хотим изменить в локальной функции глобальную
# переменную, а не определить локальную, то необходимо
# использовать ключевое слово global:

def say_bye():
    global name
    name = "Bob"
    print("Good bye", name)
