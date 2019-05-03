#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Кортежи
#

# Кортеж (tuple) представляет последовательность элементов, которая
# во многом похожа на список за тем исключением, что кортеж является
# неизменяемым (immutable) типом. Поэтому мы не можем добавлять или
# удалять элементы в кортеже, изменять его.

# Для создания кортежа используются круглые скобки, в которые
# помещаются его значения, разделенные запятыми:

user = ("Tom", 23)
print(user)

# Также для определения кортежа мы можем просто перечислить значения
# через запятую без применения скобок:

user = "Tom", 23
print(user)

# Если вдруг кортеж состоит из одного элемента, то после единственного
# элемента кортежа необходимо поставить запятую:

user = ("Tom",)

# Для создания кортежа из списка можно передать список в функцию
# tuple(), которая возвратит кортеж:

users_list = ["Tom", "Bob", "Kate"]
users_tuple = tuple(users_list)
print(users_tuple)      # ("Tom", "Bob", "Kate")

# Обращение к элементам в кортеже происходит также, как и в списке
# по индексу. Индексация начинается также с нуля при получении
# элементов с начала списка и с -1 при получении элементов с конца
# списка:

users = ("Tom", "Bob", "Sam", "Kate")
print(users[0])     # Tom
print(users[2])     # Sam
print(users[-1])     # Kate

# получим часть кортежа со 2 элемента по 4
print(users[1:4])       # ("Bob", "Sam", "Kate")

# Но так как кортеж - неизменяемый тип (immutable), то мы не сможем
# изменить его элементы. То есть следующая запись работать не будет:

try:
    users[1] = "Tim"
except:
    print('Ошибка при работе с кортежем!')

# При необходимости мы можем разложить кортеж на отдельные
# переменные:

user = ("Tom", 22, False)
name, age, isMarried = user
print(name)             # Tom
print(age)              # 22
print(isMarried)        # False

# Особенно удобно использовать кортежи, когда необходимо возвратить
# из функции сразу несколько значений. Когда функция возвращает
# несколько значений, фактически она возвращает в кортеж:


def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married


user = get_user()
print(user[0])              # Tom
print(user[1])              # 22
print(user[2])              # False

# С помощью встроенной функции len() можно получить длину кортежа:

user = ("Tom", 22, False)
print(len(user))        # 3

# Перебор кортежей

# С помощью цикла for:
user = ("Tom", 22, False)
for item in user:
    print(item)

# С помощью цикла while:
user = ("Tom", 22, False)
i = 0
while i < len(user):
    print(user[i])
    i += 1

# Как для списка с помощью выражения элемент in кортеж можно
# проверить наличие элемента в кортеже:

user = ("Tom", 22, False)
name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")

# Сложные кортежи

# Один кортеж может содержать другие кортежи в виде элементов.
# Например:

countries = (
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
)

for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {}  population: {}".format(
        countryName, countryPopulation))
    for city in cities:
        cityName, cityPopulation = city
        print("City: {}  population: {}".format(cityName, cityPopulation))

# Здесь кортеж countries, который представляет страны, состоит из
# кортежей, каждый из которых - отдельная страна.

# Вложенные кортежи имеют три элемента: название страны, численность
# ее населения и города. Города представляют отдельный кортеж, где
# каждый отдельный город - это вложенный кортеж, содержащий название
# города и численность его населения.