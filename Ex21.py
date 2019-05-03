#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Модули (сокращенно)
#

# Репозиторий модулей Python https://pypi.org/
# Команда для установки модулей sudo pip install <имя_модуля> или sudo pip3 install <имя_модуля>
# Например: sudo pip3 install pyowm

# Использование модулей STL - стандартной библиотеки

from math import pi               # импортируем константу pi модуля math
from math import sqrt             # импортируем функцию sqrt модуля math
from math import ceil as my_ceil  # имроттируем функцию ceil с переименованием в my_ceil
from math import *                # импортируем все переменные и функции модуля math
import random                     # импортируем модуль

#Случайное число

print('\nСлучайное число от 50 до 150:')
for nom in range(1, 11):
    print(str(nom) + '. ' + str(random.randint(50, 150)))