#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Открытие и закрытие файлов
#

# Чтобы начать работу с файлом, его надо открыть с помощью функции
# open(), которая имеет следующее формальное определение:

# open(file, mode)

# Первый параметр функции представляет путь к файлу. Путь файла
# может быть абсолютным, то есть начинаться с буквы диска,
# например, C://somedir/somefile.txt. Либо можно быть относительным,
# например, somedir/somefile.txt - в этом случае поиск файла будет
# идти относительно расположения запущенного скрипта Python.

# Второй передаваемый аргумент - mode устанавливает режим открытия
# файла в зависимости от того, что мы собираемся с ним делать.
# Существует 4 общих режима:

#   r (Read)    : Файл открывается для чтения. Если файл не найден,
#                 то генерируется исключение FileNotFoundError

#   w (Write)   : Файл открывается для записи. Если файл отсутствует,
#                 то он создается. Если подобный файл уже есть, то
#                 он создается заново, и соответственно старые
#                 данные в нем стираются.

#   a (Append)  : Файл открывается для дозаписи. Если файл
#                 отсутствует, то он создается. Если подобный файл
#                 уже есть, то данные записываются в его конец.

#   b (Binary)  : Используется для работы с бинарными файлами.
#                 Применяется вместе с другими режимами - w или r.

# После завершения работы с файлом его обязательно нужно закрыть
# методом close().

# Например, откроем для записи текстовый файл "hello.txt":

myfile = open("hello.txt", "w")

myfile.close()

# При открытии файла или в процессе работы с ним мы можем
# столкнуться с различными исключениями, например, к нему
# нет доступа и т.д. В этом случае программа выпадет в ошибку,
# а ее выполнение не дойдет до вызова метода close, и соответственно
# файл не будет закрыт.

# В этом случае мы можем обрабатывать исключения:

try:
    somefile = open("hello.txt", "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)

# В данном случае вся работа с файлом идет во вложенном блоке try.
# И если вдруг возникнет какое-либо исключение, то в любом случае
# в блоке finally файл будет закрыт.

# Однако есть и более удобная конструкция - конструкция with:

# with open(file, mode) as file_obj:
#     инструкции

# Эта конструкция определяет для открытого файла переменную
# file_obj и выполняет набор инструкций. После их выполнения
# файл автоматически закрывается. Даже если при выполнении
# инструкций в блоке with возникнут какие-либо исключения,
# то файл все равно закрывается.

# Так, перепишем предыдущий пример:

with open("hello.txt", "w") as somefile:
    somefile.write("hello world")
