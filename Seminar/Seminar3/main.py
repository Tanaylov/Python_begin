import os
from random import randint
clear = lambda: os.system('cls')
clear()

'''Дан список чисел. Определите, сколько в нем 
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6'''
'''
list1 = []
for i in range(50):
    list1_element = randint(1, 100)
    list1.append(list1_element)
print(*list1, sep=', ', end= ' --> ')
length = len(list1)
print(length)
#count = 0
for i in range(len(list1) - 1):
    j = i + 1
    while j < len(list1):
        if list1[i] == list1[j]:
            length -= 1
            break
        j += 1 


print(length)# - count)

set1 = set(list1)
print(*set1, sep=', ', end=' --> ')
print(len(set1))
'''
'''Дана последовательность из N целых чисел и число 
K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, K – 
положительное число.
Input: [1, 2, 3, 4, 5] k = 2
Output: [4, 5, 1, 2, 3]'''

task_list = []
task_list_result = []
user_num = int(input('Enter the number of shifts: '))

for i in range(7):
    task_list.append(i + 1)
print(task_list)

if user_num > len(task_list):
  shift_amount = (user_num - len(task_list)) % len(task_list)
  for i in range(len(task_list)):
    if shift_amount < i:
      task_list_result.append(task_list[-shift_amount + i])
    else:
      task_list_result.append(task_list[i - shift_amount])
elif user_num == len(task_list):
  task_list_result = task_list
else:
  shift_amount = user_num
  for i in range(len(task_list)):
      if shift_amount < i:
          task_list_result.append(task_list[-shift_amount + i])
      else:
          task_list_result.append(task_list[i - shift_amount])

print(task_list_result)


'''Напишите программу для печати всех уникальных 
значений в словаре. 
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
":" S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}'''
'''
task_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
#task_dict = {"X": "S001", "V": "S002", "VI": "S001", "XI": "S005", "VII": "S005", "IV": "S009",
 #             "VIII": "S007"}
print(type(task_dict), len(task_dict))
set_result = []
for el in task_dict: 
  for val in el.values():
    if val not in set_result:
      set_result.append(val)
print(set_result)
'''

'''Дан массив, состоящий из целых чисел. Напишите 
программу, которая подсчитает количество 
элементов массива, больших предыдущего (элемента 
с предыдущим номером) 
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3'''
'''
task_list = [randint(-11, 11) for i in range(11)]

print(task_list)

result = [f'({task_list[i]} < {task_list[i + 1]})' for i in range(len(task_list) - 1) if task_list[i] < task_list[i + 1]]
print(*result, ' --> ', len(result))
'''