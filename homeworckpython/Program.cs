﻿# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

dayoff = int(input('Введите число: '))
if (dayoff == 6) or (dayoff == 7):
    print('Выходной день')

if (0 <  dayoff <= 5):
    print('Будничний день')

if (dayoff > 7):
    print('Ошибка. Введите число может быть любым от 1 до 7')