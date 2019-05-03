#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Чтение текстового файла
#

# Для чтения файла открывается с режимом r (Read), и затем мы
# можем считать его содержимое различными методами:
# 
#   readline()  : считывает одну строку из файла
#   read()      : считывает все содержимое файла в одну строку
#   readlines() : считывает все строки файла в список 

# Вызовем метод readline() для чтения отдельных строк:

with open("hello.txt", "r") as file:
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2)

# Если файл небольшой, то его можно считать  методом read():

with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

# Применим метод readlines() для считывания всего файла в 
# список строк:

with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)


# При чтении файла мы можем столкнуться с тем, что его кодировка не
# совпадает с ASCII. В этом случае мы явным образом можем указать
# кодировку с помощью параметра encoding:


filename = "hello.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()

# Теперь напишем небольшой скрипт, в котором будет записывать
# введенный пользователем массив строк и считывать его обратно из
# файла на консоль:

# имя файла
FILENAME = "messages.txt"
# определяем пустой список
messages = list()

for i in range(4):
    message = input("Введите строку " + str(i+1) + ": ")
    messages.append(message + "\n")

# запись списка в файл
with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)

# считываем сообщения из файла
print("Считанные сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")
