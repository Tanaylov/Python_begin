import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

'''У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values. '''

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def transform(f, lst):
    return f(lst)
values_copy = list(map(lambda x: x, values))   #values.copy()
print(type(values_copy), values_copy)

print([int(input('enter: ')) for x in range(5)])
print(list(map(int, input('enter: ').split())))

y = (lambda x: x*7) (3)
print(y)