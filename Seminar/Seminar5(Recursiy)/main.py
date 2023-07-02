import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

''' Требуется найти N-е число Фибоначчи
Input: 7
Output: 21'''
start1 = time.time()
# def fibo(n):
#     if n in [1, 2]:
#         return 1 
#     else:
#         return fibo(n - 1) + fibo(n - 2)
def fibo2(n, left = 0, right = 1): # гораздо быстрее первого варианта с рекурсией, но всё равно медленее, чем цикл
    if n == 2:
        return right
    return fibo2(n - 1, left = right, right = right + left)
print(fibo2(15))
end = time.time() - start1
print(end)

start1 = time.time()
n = 15
fibo1 = 1
fibo2 = 1

for i in range(1, n - 2):
    fibo1, fibo2 = fibo2, fibo2 + fibo1
end = time.time() - start1
print(fibo2, end)

''' Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1'''

lst1 = [5, 3, 2, 4, 4, 3, 5, 2]
score_book = {'Vasiy': {'Math': 5, 'Language': 2, 'Chemistry': 3, 'Sport': 4}}
for key, val in score_book['Vasiy'].items():
    if val > 3:
        score_book['Vasiy'][key] = 1
print(score_book)

# def changeScore (score_list):
#     changing_list = []
#     for el in score_list:
#         if el > 3:
#             changing_list.append(1)
#         else:
#             changing_list.append(el)
#     print(changing_list)
result1 = []
min_el = min(lst1)
def changingScoreRec(lst, result, min):
    if len(lst) == 0:
        return result
    else:
        el = lst.pop(0) 
        if el > 3:
            result.append(min)
        else:
            result.append(el)
        return changingScoreRec(lst, result, min)
print(changingScoreRec(lst1, result1, min_el))

# N!:

# def factorialN(n, result = 1):
#     if n == 0:
#         return result
#     else:
#         return factorialN(n - 1, result = result * n)
def factorialN(num):
    if num == 0:
        return num + 1
    return num * factorialN(num - 1)
print(factorialN(5))


''' Напишите функцию, которая принимает одно число и 
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое 
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes'''

n = 3

def simpleNumberDetect(num, i = 3):
    flag = True
    if num == 2:
        return flag
    if num < 2 or num % 2 == 0:
        flag = False
        return flag
    if i > num // 2:
        return flag
    if num % i == 0:
        flag = False
        return flag
    return simpleNumberDetect(num, i + 2)

print(simpleNumberDetect(n))

''' Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3'''

number_list = '4568234'
print(number_list[::-1])
def reverseList (list1, result = '', i = 0):
    if i == len(list1):
        return result
    return reverseList(list1, result = result + list1[-i - 1], i = i + 1)
print(reverseList(number_list))

def reverseEnter(n):
    if n == 0: 
        return ''
    number = input('Enter the number: ')
    return reverseEnter(n - 1) + f'{number} '

count = int(input('Enter the count of elements : '))
print(reverseEnter(count))
# Полиндром:

# def polindrom (text, i = 0):
#     if i == len(text) // 2:
#         return True
#     elif text[i] != text[len(text) - 1 - i]:
#         return False
#     return polindrom(text, i + 1)
def polindromDetect(word):
    if len(word) == 0:
        return True
    if word[0] != word[-1]:
        return False
    return polindromDetect(word[1:-1])
print(polindromDetect(input('Enter the number: ')))
