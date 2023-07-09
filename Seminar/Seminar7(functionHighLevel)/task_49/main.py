import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

planet_orb = [(x, y) for x, y in orbits if x != y]
farthest = planet_orb[planet_orb.index(max(list(map(lambda x, y: x * y, planet_orb))))]
print(farthest)

# farthest = [(lambda x, y: x*y) (x, y) for x, y in orbits if x != y]
# print(*orbits[farthest.index(max(farthest))])