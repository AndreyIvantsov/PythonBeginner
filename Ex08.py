# -*- coding: utf-8 -*-

#
# Логические операции
#

# Для создания составных условных выражений применяются логические операции.
# В Python имеются следующие логические операторы:

# and (логическое умножение)
# Возвращает True, если оба выражения равны True
age = 22
weight = 58
result = age > 21 and weight == 58
print(result)  # True

# or (логическое сложение)
# Возвращает True, если хотя бы одно из выражений равно True
age = 22
isMarried = False
result = age > 21 or isMarried
print(result)  # True, так как выражение age > 21 равно True

# not (логическое отрицание)
# Возвращает True, если выражение равно False
age = 22
isMarried = False
print(not age > 21)  # False
print(not isMarried)  # True

# Для переопределения порядка вычислений мы можем использовать скобки:
age = 22
isMarried = False
weight = 58
result = (weight == 58 or isMarried) and not age > 21  # False
print(result)
