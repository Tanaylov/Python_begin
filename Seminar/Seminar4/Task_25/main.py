'''Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()'''

import os
from random import randint
clear = lambda: os.system('cls')
clear()

string = 'a a a b c a a d c d d'
# Способ решения со словарём
string_list = string.split(' ')
string_dict = dict()
#Сразу выводить на печать ничего не меняя и не создовая нового:
for el in string_list:
    if el in string_dict:
        print(f'{el}_{string_dict[el]}', end=' ')
    else:
        print(el, end=' ')
    string_dict[el] = string_dict.get(el, 0) + 1
# Создавая новы  список:
# result_list = []
# for i in range(len(string_list)):
#     if string_list[i] in string_dict:
#         result_list.append(f'{string_list[i]}_{string_dict[string_list[i]]}')
#     else:
#         result_list.append(string_list[i])
#     string_dict[string_list[i]] = string_dict.get(string_list[i], 0) + 1 
# print(*result_list)
# Тренеровка в создании словаря НЕ решение
'''set_res = set(string.split(' '))
dictinary = {}
for el in set_res:
    dictinary[el] = string.count(el)
print(dictinary)'''


# list1 = string.split(' ')
# result = [string[0]]

# print(list1)
# for i in range(1, len(list1)):
#     if list1[:i].__contains__(list1[i]):
#         element = f'{list1[i]}_{list1[:i].count(list1[i])}'
#         result.append(element)
#     else:
#         result.append(list1[i])
#     print(*result)

# Если добавить в исходную строку число, то данный алгоритм будет уже некорретно работать.
# Так как при подстчёте других символов будет добовляться цифра в строку.
# i = 1
# length = len(string)
# while i < length:
#     if string[i] == ' ':
#         i += 1
#         continue
#     if string[i] in string[:i]:
#         n = f'_{str(string[:i].count(string[i]))}'
#         string = f'{string[:i + 1]}{n}{string[i + 1:]}'
#         i += 3
#         length += 2  
#         print(string)  
#     else:
#         i += 1
