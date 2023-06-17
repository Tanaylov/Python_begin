# number = int(input('Enter a number: '))
# print(number * 2)

# number1 = -1
# while 0 >= number1 or number1 > 9:
#   number1 = int(input("Enter a number: "))
#   if 0 >= number1 or number1 > 9:
#     print('You entered incorrect number. From 1 to 9, please.')
# print(number1)  

medical_list = []

for record in range(4):
  if record == 0:
    print('Enter your name:')
    medical_list.append(input())
  elif record == 1:
    print('Enter your surname:')
    medical_list.append(input())
  elif record == 2:
    print('Enter your age:')
    medical_list.append(int(input()))
  elif record == 3:
    print('Enter your weight:')
    medical_list.append(int(input()))
print(medical_list)
''' Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
Все остальные варианты вы можете обработать на ваш вкус и полет фантазии. '''

if medical_list[2] <= 30 and 50 <= medical_list[3] < 120:
  print(f'Good condition {medical_list[0]} {medical_list[1]}.')
elif 30 < medical_list[2] <= 40 and (50 >= medical_list[3] or medical_list[3] > 120):
  print(f'{medical_list[0]} {medical_list[1]} need to exercise.')
elif medical_list[2] > 40 and (50 > medical_list[3] or medical_list[3] > 120):
  print(f'{medical_list[0]} {medical_list[1]} needs medical care.')
else:
  print("Outside the context.")

