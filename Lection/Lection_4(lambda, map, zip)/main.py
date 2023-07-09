import os
import time
from random import randint
clear = lambda: os.system('cls')

def sum1(a, b = 0):
    return a + b

print(sum1(5, 11))

sum11 = lambda a, b = 0: a + b
print(sum11(4, 15))

lst1 = [1, 2, 3, 5, 8, 15, 23, 38]

def squareEvenNum(lst):
    return [(a, a*a) for a in lst if a % 2 == 0]
lst2 = list(map(lambda a: a % 2 == 0, lst1))
print(lst2)

lst3 = list(map(int, input('Enter the number from space: ').split(' ')))
print(lst3)

# HW:
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

table1 = Table(lambda x, y: (x + y) * 2, 6, 6)
print(table1)
printTable(table1)    

