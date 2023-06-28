import os
from random import randint
import time
clear = lambda: os.system('cls')
clear()

text = 'osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen' # '253235235a5323352n25235352t253523523235oo235523523523n' 
# 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon'

anton = 'anton'
start = time.time()
# Если убрать сначала лишние элементы программа работает быстрее:
for el in text:
    if el not in anton:
        text = text.replace(el, '') 
print(text)
index_anton = 0
i = 0
while i < len(text):
    if anton[index_anton] in text[i:]:
        i = text[i:].find(anton[index_anton]) + len(text[:i]) + 1
        index_anton += 1
        if index_anton == len(anton):
             print('The refrigerator is infected with a virus')
             break
        print(i, index_anton)
    else:
      i += 1
end = time.time() - start
print(end)
   
    