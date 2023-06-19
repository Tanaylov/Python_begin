'''Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
не превосходящие числа N.'''
import os
from random import randint

clear = lambda: os.system('cls')
clear()

while True:
    user_number = input('Number, please: ')
    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print('Wrong enter, try again.')

result_string = ''
for i in range(user_number):
    result = 2 ** i
    if result == user_number:
        result_string += f'{result}'
        print(f'{user_number} ---> {result_string}')
        break
    elif result > user_number:
        print(f'{user_number} ---> {result_string[:-2]}')
        break
    result_string += f'{result}, '



