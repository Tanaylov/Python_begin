import os
from random import randint
clear = lambda: os.system('cls')
clear()
# import modul1
# from modul1 import max1
# from modul1 import * # Import all functions
import modul1 as m1 # программно переименовали файл для удобства
print(m1.max1(3, 11))
# print(modul1.max1(5, 7))

# Функция суммы от одного до N:
number1 = 9
def sumFrom1ToNumber(number, word = 'Hello'): 
# Можно по умолчанию передать переменной какое-то значение и при вызове можно это значение изменить
    print(word)
    result_sum = 0
    for i in range(1, number + 1):
        result_sum += i
        # print(result_sum)
    return result_sum

res = sumFrom1ToNumber(number1, 'Result: ')
print('tot')
print(res)

# В функцию можно передать неограниченное количество аргумернтов с иомощью '*':
def string(*args):
    result = ''
    for i in args:
        result += str(i)
    return result

print(string(1, 5, 3))
        
# Рекурсия:
def fibonachi(num):
    if num in [1, 2]:
        return 1
    else:
        return fibonachi(num - 1) + fibonachi(num - 2)

print(fibonachi(9))




