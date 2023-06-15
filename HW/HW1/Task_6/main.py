'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no'''

import os
clear = lambda: os.system('cls')
clear()

number = input('Enter 6 digits number: ')
summ_left = 0
summ_right = 0
# Вариант с for:
# for digit in number[:3]:
#   summ_left += int(digit)
# for digit1 in number[3:]:
#   summ_right += int(digit1)

size = len(number)
while size != 0:
  if size > len(number) / 2:
    summ_right += int(number[size - 1])
  else:
    summ_left += int(number[size - 1])
  size -= 1

if summ_left == summ_right:
  print('Your ticket is lucky!')
else:
  print("Your ticket is usual")

