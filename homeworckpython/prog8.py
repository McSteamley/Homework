# Вычислить число пи c заданной точностью d
#from cmath import pi
#import math
#print(round(math.pi, 2))

import math
N = int(input("Введите количество цифр после запятой:"))
print("Число 𝜋: {:.45f}".format(math.pi))
x  = math.pi
y = round(x,N+1)*10**N
z = math.modf(y)
x = z[1] / 10**N
print("Число 𝜋 с заданной точностью:", x)



# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input('Введите натуральное число: '))
lst = []
x = 2
while x * x <= N:
    if N % x == 0:
        lst.append(x)
        N = N // x
    else:
        x = x + 1
if N >= 1:       
    lst.append(N)
print(lst)



# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = [5, 8, 6, 5, 3, 8, 1, 0, 6]
lst1 = []
count = 0
for i in lst:
    if lst.count(i) == 1:
        lst1.append(i)
        count = count + 1
print(f'{lst} => {lst1}')



# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


from random import randint
from sympy import symbols
from math import prod

max_val = 100
k = int(input('Введите натуральную степень:'))
factor = [randint(-max_val, max_val) for i in range(k)]+[randint(1, max_val)]
x = symbols('x')
result = sum(map(prod,zip(factor,[x**i for i in range(k+1)])))
print(f'{result} = 0')

with open('ЗАДАЧА4.txt', 'w') as my_file:
    my_file.write(f'{result} = 0')



30*x**5 + 92*x**4 - 19*x**3 - 56*x**2 + 5*x + 92 = 0