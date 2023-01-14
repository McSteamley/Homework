# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
txt = input("Введите текст через пробел: ")
print(f'Исходный текст: {txt}')
find_text = "абв"
lst = [i for i in txt.split() if find_text not in i]
print(f'Результат: {" ".join(lst)}')




#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#a) Добавьте игру против бота

#b) Подумайте как наделить бота ""интеллектом""

from random import randint

print("*" * 9, "Играет бот и игрок", "*" * 9)
igrok1 = input("Введите имя игрока: ")
igrok2 = 'Bot'
result = int(input("Введите количество конфет на столе: "))
counter1 = 0 
counter2 = 0
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {igrok1}")
else:
    print(f"Первый ходит {igrok2}")

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, result):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {result} конфет.")

while result > 28:
    if flag:
        k = input_dat(igrok1)
        counter1 += k
        result -= k
        flag = False
        p_print(igrok1, k, counter1, result)
    else:
        k = randint(0, 28)
        counter2 += k
        result -= k
        flag = True
        p_print(igrok2, k, counter2, result)

if flag:
    print(f"Выиграл {igrok1}")
else:
    print(f"Выиграл {igrok2}")



#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#a) Добавьте игру против бота

#b) Подумайте как наделить бота ""интеллектом""

from random import randint
print("*" * 9, "Играют 2 игрока", "*" * 9)
igrok1 = input("Введите имя первого игрока: ")
igrok2 = input("Введите имя второго игрока: ")
result = int(input("Введите количество конфет на столе: "))
counter1 = 0 
counter2 = 0
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {igrok1}")
else:
    print(f"Первый ходит {igrok2}")

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, result):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {result} конфет.")

while result > 28:
    if flag:
        k = input_dat(igrok1)
        counter1 += k
        result -= k
        flag = False
        p_print(igrok1, k, counter1, result)
    else:
        k = input_dat(igrok2)
        counter2 += k
        result -= k
        flag = True
        p_print(igrok2, k, counter2, result)

if flag:
    print(f"Выиграл {igrok1}")
else:
    print(f"Выиграл {igrok2}")



# Создайте программу для игры в ""Крестики-нолики"".
print("*" * 9, "Классическая игра Крестики-Нолики ", "*" * 9)
 
board = list(range(1,10))
wins_positions = [(1,2,3), (4,5,6), (7,8,9), (1,4,7,), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

def draw_board():
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)


def take_input(player_token):
   while True:
      value = input("Куда поставить: " + player_token + "?")
      if not (value in "123456789"):
         print("Ошибка ввода. Повторите, пожалуйста!")
         continue
      value = int(value)
      if str(board[value - 1]) in "XO":
         print("Данная клетка уже занята!")
         continue
      board[value - 1] = player_token
      break

def check_win():
   for each in wins_positions:
      if(board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
         return board[each[0] - 1]
   else:
      return False


def main():
   counter = 0
   while True:
      draw_board()
      if counter % 2 == 0:
         take_input("X")
      else:
          take_input("O")
      if counter > 3:
         winner = check_win()
         if winner:
            draw_board()
            print(winner, "выиграл!")
            break
      counter += 1
      if counter > 8:
         draw_board()
         print("Ничья!")
         break
   
main()




# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('encoding.txt', 'w', encoding='UTF-8') as my_file:
    my_file.write(input('Введите текст для сжатия: '))
with open('encoding.txt', 'r') as my_file:
    my_txt = my_file.readline()
    txt_compress = my_txt.split()

print(my_txt)

def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


txt_compress = file_encod(my_txt)

with open('coding.txt', 'w', encoding='UTF-8') as my_file:
    my_file.write(f'{txt_compress}')
print(txt_compress)




