"""
n = 5
nothing = None
floating_number = 1.4
word2 = 'Helloooo!'
print(n, floating_number, word2, nothing)
print(f"{n} - {nothing} - {word2}")
print("{} - {} - {} - {}".format(floating_number, n, word2, nothing))
# n = 'fd'

word = "ty'pe"
word1 = 'ty\'pe'
type1 = type(n)
print(type1, word, '++', word1)
"""
# text = 'Enter second number: ' 
# print("Enter first number: ")
# user1 = input()
# user2 = input(text)
# user3 = float(input('Enter third number: '))
# summ = float(int(user1) + int(user2) + user3)
# print(user1, user2, ' = ', summ)
'''
number = 5.89
sum = number - int(number)
print(sum)

number2 = 1.55
number3 = 5.897
action = number2/number3
print(round(action, 2))
action += 3
print(action)

number4 = 123456
text_number4 = str(number4)
summ = 0
for digit in text_number4:
  summ += int(digit)
print(summ)

number4 = 123456
summ = 0
while number4 > 0:
  if summ == 11:
    break
  summ += number4 % 10
  number4 //= 10
else:
  summ /= 7
print(summ)

i = 0
while i < 5:
  # if i == 3:
  #   break
  i += 1
else:
  print('fhfh')
print(i)

user_input = int(input("Enter the number: "))
flag = True
minimum_divisor = 2
while(flag):
  if user_input % minimum_divisor == 0:
    print(minimum_divisor)
    flag = False
  elif minimum_divisor > user_input // 2:
    print(user_input)
    flag = False
  minimum_divisor += 1
'''
sum = 0
for el in range(-100, 0, 25):
  sum += el
print(sum)
r = range(10)
#list = []
text = ""
for i in r:
  i = str(i) + 'a, '
  text +=i
#  list.append(i)
#print(list)
print(text[0: len(text) - 2])
print(text.upper())
print('6' in text)
print(text.replace('a', 'B').lower())

print(*[i for i in r])

for i in range(5):
  print(i)