import os
from random import randint
clear = lambda: os.system('cls')
clear()
# 60
# print('Think of the number.')
# input()
# user_number = None
# min_num_value, max_num_value = 1, 100
# while True: 
#   num = randint(min_num_value, max_num_value + 1)
#   print(num)
#   user_answer = input()
#   if user_answer == 'yes':
#     user_number = num
#     print('Victory!', user_number)
#     break
#   elif user_answer == '>':
#     min_num_value = num + 1
#   else:
#     max_num_value = num
computer_num = randint(1, 101)
difficulty = int(input('Choose the difficult(number of try): '))
print(computer_num)
my_number = int(input('Number: '))
i = 1
while my_number != computer_num:
    if my_number > computer_num:
        my_number = int(input('You need a smaller number: '))
    else:
        my_number = int(input('You need a bigger number: '))
    i += 1
    if i == difficulty:
         print('You lose big boy!!!')
         break
else:
        print('You win!')
     

'''
lst1 = [i for i in range(7, 1, -1)]
print(lst1)
dictin1 = set(lst1)
print(dictin1)

lst2 = [(x, y, z) for x in range(1, 5) for y in range(5, 18) for z in range(2,5)]

print(lst2, len(lst2))
'''
