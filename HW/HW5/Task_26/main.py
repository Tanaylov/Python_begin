'''Задача 26:  Напишите программу, 
которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''

# 1-ый способ:
a = 6
b = 4

def aToExtentOfb (a, b, c = a):
    if b == 1:
        return a
    else:
        return aToExtentOfb(a*c, b - 1, c)
print(aToExtentOfb(a, b))

# 2-ой способ(как я понимаю, более правельный):

# a = 6
# b = 3

# def aToExtentOfb (a, b):
#     if b == 1:
#         return a
#     else:
#         return a*aToExtentOfb(a, b - 1)

# print(aToExtentOfb(a, b))





