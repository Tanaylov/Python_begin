import os
clear = lambda: os.system('cls')
clear()
while True:
    user_date = input('Enter the date(format: dd.mm.yyyy): ')
    if '.' in user_date and user_date.isdigit:
         user_date = user_date.split('.')
         break
    else:
         print('Incorrect format for date.')  
print(user_date)
year = user_date.pop()
print(user_date, year)
day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртное', '05': 'пятое', 
       '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое',
       '10': 'десятое', '11': '', '12': '', '13': '', '14': '', '15': '', 
       '16': '', '17': '', '18': '', '19': '',
       '20': '', '21': '', '22': '', '23': '', '24': '', 
       '25': '', '26': '', '27': ''}
month = {'01': 'Января', '02': 'Февраля', '03': 'марта', '04': 'апреля', '05': 'мая'}

user_day = f'{day[user_date[0]]} {month[user_date[1]]} {year}' 
print(user_day)