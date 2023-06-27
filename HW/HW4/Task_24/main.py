'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод 
— на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.'''
import os
from random import randint
clear = lambda: os.system('cls')
clear()

bed_count = 11
bush_list = [randint(15, 25) for i in range(bed_count)]
print(bush_list)
# Так как работ собирает с соседних кустов, то нужно учесть момент сбора с первого и последнего куста.
# Я искусственно добавляю последний куст перед первым и первый после последнего.
bush_list.insert(0, bush_list[-1])
bush_list.insert(bed_count + 1, bush_list[1])
print(bush_list)
word_bush = ' bush'
berry_count = dict()
for i in range(1, bed_count + 1):
    key = str(i) + word_bush
    berry_count[key] = bush_list[i] + bush_list[i - 1] + bush_list[i + 1]
print(berry_count)

bush_number, maximum_berry_picking = '', 0 
for k, v in berry_count.items():
    if v > maximum_berry_picking:
        maximum_berry_picking = v
        bush_number = k

# bush_number = max(berry_count, key=berry_count.get)
# maximum_berry_picking = max(berry_count.values())

print(f'From {bush_number} we get maximum berreis: {maximum_berry_picking}')  