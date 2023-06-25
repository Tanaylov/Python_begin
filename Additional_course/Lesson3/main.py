import os
from random import randint
clear = lambda: os.system('cls')
clear()

lst1 = [i for i in range(7, 1, -1)]
print(lst1)
dictin1 = set(lst1)
print(dictin1)

lst2 = [(x, y, z) for x in range(1, 5) for y in range(5, 18) for z in range(2,5)]

print(lst2, len(lst2))