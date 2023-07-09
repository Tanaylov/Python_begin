'''Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам '''

import os
import time
from random import randint
clear = lambda: os.system('cls')
clear()

#phrase = 'пара-ра-рам рам-пам-папуам па-ра-па-да'
phrase = list(map(str, input('Type the phrase with a space: ').split()))
vowels = 'ауеыоэяию'

def rhythmTest(lst, vowels):
    lst_vow = []
    for el in lst:
        string_vowels = ''
        for i in range(len(el)):           
            if el[i] in vowels:
                string_vowels += f'{el[i]}'
        lst_vow.append(string_vowels)
        if len(lst_vow) > 1 and len(lst_vow[-1]) != len(lst_vow[-2]):
            return 'Пам парам'
    return 'Парам пам-пам'

            
#phrase_list = phrase.split() 
print(rhythmTest(phrase, vowels))
