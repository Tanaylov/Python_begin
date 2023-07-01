import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

''' Требуется найти N-е число Фибоначчи
Input: 7
Output: 21'''
start1 = time.time()
def fibo(n):
    if n in [1, 2]:
        return 1 
    else:
        return fibo(n - 1) + fibo(n - 2)
print(fibo(7))
end = time.time() - start1
print(end)

start1 = time.time()
n = 37
fibo1 = 1
fibo2 = 1

for i in range(1, n - 2):
    fibo1, fibo2 = fibo2, fibo2 + fibo1
end = time.time() - start1
print(fibo2 + fibo1, end)

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
print(factorialN(1))


tuple1 = '4567893'
def reverse(list1, n = 0):
    
    if n == len(list1)//2:
        return list1
    
    return reverse(list1, n - 1)
print(reverse(tuple1))