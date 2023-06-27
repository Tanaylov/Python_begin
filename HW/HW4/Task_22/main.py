''' Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств. '''

import os
from random import randint
clear = lambda: os.system('cls')
clear()

# Решение через множества:
'''size1 = int(input('Enter the size of the first set: '))
size2 = int(input('Enter the size of the second set: '))

print('Enter the values for first set: ')
set1 = {int(input()) for i in range(size1)}
print('Enter the values for second set: ')
set2 = {int(input()) for i in range(size2)}

print('First set: ', *set1) 
print('Second set: ', *set2)
set_result = set1 & set2
# Как я понял, если нет отрицательного элемента во множестве, 
# то оно автоматом сортируется от меньшего к большему. Если есть, то сортируется сначало 
# положительные элементы, а потом идут тоже отсортированные отрицательные элементы. Но лучше всё равно 
# использовать sorted(), т. к. иногда почему-то он не сортирутется как надо.
set_result = sorted(set_result)
print(*set_result)'''


# Решение через списки:
size1 = int(input('Enter the size of the first set: '))
size2 = int(input('Enter the size of the second set: '))
list1 = []
list2 = []
print('Enter the values for first list:')
i = 0
while i < size1:
  while True:
    element = input()
    if element[0] == '-':
       element = element[1:]
    if element.isdigit():
       element = int(element)
       break
    else:
       print('You enter incorrect number, try again', end=': ')
  if list1.__contains__(element): # Сразу убираю повторы
      size1 -= 1
      continue
  else:
      list1.append(element)
  i += 1

print('Enter the values for second list:')
i = 0
while i < size2:
  while True:
    element = input()
    if element[0] == '-':
       element = element[1:]
    if element.isdigit():
       element = int(element)
       break
    else:
       print('You enter incorrect number, try again', end=': ')
  if list2.__contains__(element):
      size2 -= 1
      continue
  else:
      list2.append(element)
  i += 1

print(f'First sequence: {list1}') 
print(f'Second sequence: {list2}')

result_list = []
# собираю список одинаковых элементов из двух списков
if len(list1) < len(list2): # ввёл условие, чтобы идти по списку с минимальной длиной
   for el in list1:
      if el in list2:
         result_list.append(el)
         i = len(result_list) - 1 # сразу при компановке нового списка сортирую его min->max
         while i != 0:
            if result_list[i - 1] > result_list[i]:
               result_list[i - 1], result_list[i] = result_list[i], result_list[i - 1]
            i -= 1
else:
   for el in list2:
      if el in list1:
         result_list.append(el)
         i = len(result_list) - 1
         while i != 0:
            if result_list[i - 1] > result_list[i]:
               result_list[i - 1], result_list[i] = result_list[i], result_list[i - 1]
            i -= 1

print('Result sequence', end=': ')
print(*result_list, sep=', ')