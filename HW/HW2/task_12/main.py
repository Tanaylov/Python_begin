'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.'''

import os
import time
from random import randint
# 7 100
clear = lambda: os.system('cls')
clear()
start = time.time()

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

end = time.time() - start
print(end)
# Почему не работал такой вариант?:
# while number_x + number_y != summ_s and number_x * number_y != product_p:


# Задача 12 (пример решения - эталонное решение)
start = time.time()

x = int(input())
y = int(input())
flag = False
for i in range(x):
    for j in range(y): # до x (faster)
        if x == i + j and y == i * j:
            print(i, j)
            flag = True
            break
    if flag == True:
        break
            

end = time.time() - start
print(end)