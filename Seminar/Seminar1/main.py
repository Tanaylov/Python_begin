# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 
# Output: 2

# n = int(input('сколько км проезжает машина в день: '))
# m = int(input('введите длину маршрута: '))

# # print(f"нужно дней: {-(-m // n)}")
# print(f"нужно дней: {(m // n) + (m % n != 0)}")

''' В некоторой школе решили набрать три новых 
математических класса и оборудовать кабинеты для 
них новыми партами. За каждой партой может сидеть 
два учащихся. Известно количество учащихся в 
каждом из трех классов. Выведите наименьшее 
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32 '''
# import math

# classes = [15, 23, 25, 15, 19, 20]
# desks3 = 0
# desks4 = 0
# for clas in classes:
#    desks4 += math.ceil(clas / 2)
# print(desks4)

# for clas in classes:
#    desks3 += clas // 2 + clas % 2
# print(desks3)
# class1 = 7; class2 = 23; class3 = 23
# desks1 = (class1//2 + class2//2 + class3//2) + (class1%2 != 0) + (class2%2 != 0) + (class3%2 != 0)
# desks2 = (class1//2 + class2//2 + class3//2) + class1%2 + class2%2 + class3%2

# print(desks1, desks2) 

# your_number = 5; current_number = 7; wagon_value = 0
# if your_number == current_number:
#   print("Not enough information.")
# else:
#   wagon_value = current_number + your_number - 1
# print(wagon_value)

''' Задача №7. Решение в группах
Дано натуральное число. Требуется определить, 
является ли год с данным номером високосным. Если 
год является високосным, то выведите YES, иначе 
выведите NO. Напомним, что в соответствии с 
григорианским календарем, год является 
високосным, если его номер кратен 4, но не кратен 
100, а также если он кратен 400.
Input: 2016
Output: YES'''

import os
from random import randint
clear = lambda: os.system('cls')
clear()

year = 2000
if year % 4 == 0 and year & 100 != 0 or year % 400 == 0:
  print(f"{year} is Leap year.")
else:
  print(f'{year} is usual year.')