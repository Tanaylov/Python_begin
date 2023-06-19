'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.'''

import os
from random import randint

clear = lambda: os.system('cls')
clear()
number_x = 0; number_y = 0
print('Think of numbers and write the sum(S) and product(P) of them.')
sum_s = int(input('Enter the S: '))
product_p = int(input('Enter P: '))
flag = True
while flag:
    number_y = randint(1, sum_s); number_x = randint(1, sum_s)
    if number_x + number_y == sum_s and number_x * number_y == product_p:
      flag = False
print(number_x, number_y)

# Почему не работал такой вариант?:
# while number_x + number_y != summ_s and number_x * number_y != product_p:
