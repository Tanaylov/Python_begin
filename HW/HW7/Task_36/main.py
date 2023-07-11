'''Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны 
быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36 '''
import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

def func(x, y):
    return x * y

def randomVal(x, y):
    x, y = randint(1, 11), randint(1, 11)
    return x + y

def Table(f, row, column):
    table = []
    for i in range(1, row + 1):
        table1 = []
        for j in range(1, column + 1):
            table1.append(f(x = i, y = j))
        table.append(table1)
    return table

def printTable(table):
    for i in range(len(table)):       
        for j in range(len(table[i])):
            if -10 < table[i][j] < 10:
              print(table[i][j], '  | ', end='')
            else:
              print(table[i][j], ' | ', end='')
        print()

table1 = Table(lambda x, y: x * y, 6, 6) # Table(randomVal, 6, 6) # Table(func, 7, 3)
print(table1)
printTable(table1)

