# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 

def SomeNumbers(j):
    xyz = ["X", "Y", "Z"]
    lst = []
    for i in range(j):
        lst.append(input(f"Введите значение {xyz[i]}: "))
    return lst


def Predicates(j): # сравнения левой части с правой
    left_side = not (j[0] or j[1] or j[2])
    right_side = not j[0] and not j[1] and not j[2]
    result = left_side == right_side
    return result


confirmation = SomeNumbers(3) 

if Predicates(confirmation) == True:
    print(f"Истина")
else:
    print(f"Ложь")