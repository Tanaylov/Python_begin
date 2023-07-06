''' Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:       Вывод:
1 2 3 2 3   2
'''

import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()
task_lst = [8, 8, 1, 2, 4, 2, 5, 8, 1, 4, 2, 2, 1, 5, 5]
count = 0
repeat_el = []
for el in task_lst:
    if task_lst.count(el) > 1:
        if el not in repeat_el:
          repeat_el.append(el)
          count += task_lst.count(el) // 2
        
print(count, repeat_el)
