import os
clear = lambda: os.system('cls')
clear()
'''
task_list = list()
search_num = 5
count, count1 = 0, 0
for i in range(4):
    task_list.append(int(input('Set the value of the list item: ')))
    if search_num in task_list[i:]: 
        count += 1
    if search_num == task_list[i]:
        count1 += 1

print(*task_list, "-->", count, count1)

search_num1 = 7
close_value_num = None
min_value, max_value = min(task_list), max(task_list)
if search_num1 in task_list:  #task_list.__contains__(search_num1):
    close_value_num = search_num1
    print(close_value_num)
else:   
  for el in task_list:
      if min_value < el < search_num1:
          min_value = el
      if max_value > el > search_num1:
          max_value = el
  print(max_value, min_value)
  if (max_value - search_num1) < (search_num1 - min_value):
      close_value_num = max_value
  else:
      close_value_num = min_value
  print(close_value_num)
'''
'''В случае с английским алфавитом очки распределяются так:

A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков. '''
import time
dict1 = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
dict2 = dict.fromkeys(['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'], 2)
dict3 = dict.fromkeys(['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
dict4 = dict.fromkeys(['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'], 4)
dict5 = dict.fromkeys(['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
dict8 = dict.fromkeys(['J', 'X', 'Ш', 'Э', 'Ю'], 8)
dict10 = dict.fromkeys(['Q', 'Z', 'Ф', 'Щ', 'Ъ'], 10)

dict_scrabl = dict(dict1|dict2|dict3|dict4|dict5|dict8|dict10)
start = time.time()

user_word = input('Enter the word to count your score in Scrabble: ').upper()
score = 0
for letter in user_word:
    score += dict_scrabl[letter]

print(score)
end = time.time() - start
print(end)
c = {1: ['peanut','butter','jelly','time'], 2:['fish','chips']}
d = {1: ['fish','chips'], 2:['peanut','butter','jelly','time']}
# key1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
# value1 = [1, 1, 1, 1, 1, 1, 1, 1, 1,]
#dict_scrabl = zip(key1, value1)
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
start = time.time()
k = 'lizard'
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_ru:
            if i in points_ru[j]:
                count = count + j
print(count)

end = time.time() - start
print(end)