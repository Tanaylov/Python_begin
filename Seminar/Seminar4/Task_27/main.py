import os
from random import randint
clear = lambda: os.system('cls')
clear()

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

text = text.upper()
text_list = text.split(' ')
print(text_list)
text_list = set(text_list)
print(text_list)

print(len(text_list))