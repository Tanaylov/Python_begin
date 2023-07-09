'''Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

print('Enter the input data for arithmetic progression.')
def userInputIsNumber(text, error, only_positive = True):    
  if only_positive:  
    while True:
      num = input(text)
      if num.isdigit():
        return int(num)
      else:
        print(error)
  else: 
    while True: 
        num = input(text)
        if (num[0] == '-' and num[1:].isdigit()) or num.isdigit():
          return int(num)
        else:
          print(error)

error_enter = 'You enter incorrect number.'
first_num = userInputIsNumber('Enter the first number (a1) in progression', error_enter, False)
diff = userInputIsNumber('Enter the difference (d): ', error_enter, False)
num_count = userInputIsNumber('Enter the count of element (n): ', error_enter)  

num_arithmetic_progression = [first_num + num_count * diff for num_count in range(num_count)]
print(*num_arithmetic_progression, sep=', ')

first_num = 2; delta = 7; count_el = 11
arithmetc_prog = [x for x in range(first_num, delta * count_el, delta)]
print(arithmetc_prog)
