'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) '''
import os
clear = lambda: os.system('cls')
clear()

# Первый вариант:
user_number = input('Enter a whole number: ')
summa = 0
for digit in user_number:
  summa += int(digit)
print(f"Summ digits in {user_number} is {summa}")

# Второй вариант:
print('Enter a whole number(integer):')
user_number1 = int(input())
user_number11 = user_number1
summ = 0
while user_number1 > 0:
  summ += user_number1 % 10
  user_number1 //= 10
print("Summ digits in {} is {}".format(user_number11, summ))