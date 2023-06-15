'''Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов,
a Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10'''
import os
clear = lambda: os.system('cls')
clear()

from random import randint
flag = True
while flag:
  number = randint(10, 100)  
  if number % 6 == 0: 
    flag = False   

coefficient = number // 6
count_Peter_and_Sergey = coefficient
coefficient += coefficient
count_Kate = coefficient * 2
print(number, ' --> ', count_Peter_and_Sergey, count_Kate, count_Peter_and_Sergey)