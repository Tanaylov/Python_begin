''' Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no '''

import os
clear = lambda: os.system('cls')
clear()

from random import randint

num1 = randint(2, 7)
num2 = randint(2, 7)
num3 = randint(5, 13)
print(num1, num2, num3)

if num3 > num1 * num2:
  print('The chocolate is too small for so many slices')
elif num3 < num1 * num2 and num3 % num2 == 0 or num3 % num1 == 0:
  print('Yes')
else:
  print('No')
