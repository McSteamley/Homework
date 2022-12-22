# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [1, 2, 8, 7, 3]
sum_ = 0
i = 0
for i in range(len(lst)):
    if i % 2 == 1:
        sum_ = sum_ + lst[i]
print(f'\nСумма равна:{sum_}')



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# Введём 2 списка, где lst1 содержит чётное количество чисел, а lst2 - нечётное количество чисел
lst1 = [4, 1, 3, 2]
lst2 = [4, 1, 3, 2, 6]
lst3 = []
lst4 = []
multi1 = 1
multi2 = 1
i = 0
N = 0

for i in range(len(lst1)//2):# Алгоритм нахождения произведения пар чисел для списка с чётным количеством элементов(lst1)
        multi1 = (lst1[i] * lst1[N - i - 1])
        lst3.append(multi1)

for i in range(len(lst2)//2+1):# Алгоритм нахождения произведения пар чисел  для списка с нечётным количеством элементов(lst2)
        multi2 = (lst2[i] * lst2[N - i - 1])
        lst4.append(multi2)

print(lst3)
print(lst4)




# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [2.4, 6.8, 1.9, 0.456, 4.25, 3.08]
max = 0
min = 1
result = 0
for i in range(len(lst)):
    x = lst[i] % 1  + 0.0001
    if x > max:
        max = x
    elif x == 0.001:
        print('Совпадение')
    elif x < min:
        min = x
result = max - min
print(f'{lst} => {result:.2f}')



# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)




# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input('Введите целое число:'))
neg_fibo = []
fibo = []
together_fibo = []
neg_fibo.append(1)
fibo.append(0)
fibo.append(1)
n = 1
for i in range(k - 1):
    n = - n
    fib = fibo[i] + fibo[i + 1]
    fibo.append(fib)
    neg_fibo.append(fib * n)
neg_fibo.reverse()
together_fibo = neg_fibo + fibo
print(f'Для k = {k} => {together_fibo}')

