''' Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 10**5
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод: Вывод:
300   220 284 '''
import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

k = 300
def frendly_num(num1, num2):
    if num1 == num2:
       return False
    else:
        num1_dividers = [div for div in range(1, num1 // 2 + 1) if num1 % div == 0]
        num2_dividers = [div for div in range(1, num2 // 2 + 1) if num2 % div == 0]
        if sum(num1_dividers) == sum(num2_dividers) and len(num1_dividers) != 1:
            return True
        return False
res_lst = []
for i in range(k):
    for j in range(k):
      if frendly_num(i, j):
        res_lst.append((i, j))

print(res_lst)
