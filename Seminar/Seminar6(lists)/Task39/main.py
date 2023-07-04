'''Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит 
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод:           Вывод: 3 3 2 12
7 
3 1 3 4 2 4 12
6
4 15 43 1 15 1 '''
import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

lst1 = [3, 1, 3, 4, 2, 4, 12]
lst2 = [4, 15, 43, 1, 15, 1]
my_set = set(lst1) - set(lst2)
print(my_set)
result = []
for el in lst1:
    if el  not in lst2:
        result.append(el)
print(result)
length = len(lst1)
i = 0
while i < length:
    if lst2.__contains__(lst1[i]):
        del lst1[i] 
        length -= 1
    else:
        i += 1
print(lst1)
lst1.extend(lst2)
print(lst1)
lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)