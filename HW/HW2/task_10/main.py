'''Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть. '''
import os
clear = lambda: os.system('cls')
clear()

from random import randint
size = randint(5, 15)
coin_list = []
coin_side1 = 0; coin_side2 = 1
count_side1 = 0; count_side2 = 0
for i in range(size):
  coin_list.append(randint(0, 1))
  if coin_list[i] == coin_side1:
    count_side1+=1
  else:
    count_side2+=1

if count_side2 > count_side1:
  print(f'{coin_list}, {size} --> optimal number of actions: {count_side1} ({coin_side1}).')
else:
  print(f'{coin_list}, {size} --> optimal number of actions: {count_side2} ({coin_side2}).')



size = randint(5, 15)
coin_string = ''
coin_side1 = '0'; coin_side2 = '1'
for i in range(size):
  coin_string += f'{randint(0, 1)}'
print(', '.join(coin_string), end=' - ') 

count1 = coin_string.count(coin_side1)
count2 = coin_string.count(coin_side2) 

if  count1 > count2:
  print(f'{size} --> optimal number of actions: {count2} ({coin_side2})')
else:
  print(f'{size} --> optimal number of actions: {count1} ({coin_side1})')



