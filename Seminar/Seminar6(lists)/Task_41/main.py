'''Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве 
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод:       Ввод:
5           5
1 2 3 4 5   1 5 1 5 1
Вывод:      Вывод:
0           2     '''
import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

task_list = [2, 4, 3, 5, 6, 11, 12, 11, 4, 23, 1]
task_list = [3, 2, 5, 1, 5, 1]
count = 0
i = 1

while i < len(task_list) - 1:
    if task_list[i] > task_list[i - 1] and task_list[i] > task_list[i + 1]:
        count += 1
        i += 2
    else:
        i += 1
    
print(count)

