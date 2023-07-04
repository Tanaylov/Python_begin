'''Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''
import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

  
def getSortedList(length):    
  lst = []
  for i in range(length):
    lst.append(randint(-11, 11))
    if i!= 0:
      k = i 
      while k != 0:
        if lst[k] < lst[k - 1]:
          lst[k], lst[k - 1] = lst[k - 1], lst[k]
        k -= 1
  return lst
def getIndexInRange(lst, min, max):
  if min > lst[-1] or max < lst[0]:
    print('There is not found elements in list from the current value range.')
  else:
    index_list = [i for i in range(len(lst))
                  if lst[i] >= min and lst[i] <= max]
    if len(index_list) == 0:
      print('There is not found elements in list from the current value range.')
    else:
      print(*index_list, sep=', ')
      return index_list

len_list = 7
origin_list = getSortedList(len_list)
while True:
  condition_left = randint(-5, 2)
  condition_right = randint(3, 11)
  if condition_left <= condition_right:
    break

print(*origin_list, sep=', ')
print('Range:', condition_left, ' - ', condition_right)
getIndexInRange(origin_list, condition_left, condition_right)
