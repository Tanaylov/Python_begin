import os
clear = lambda: os.system('cls')
clear()

user_date = input('Enter the date(format: dd.mm.yyyy): ').split('.')
print(user_date)
year = user_date.pop()
print(user_date, year)
day = {'01': 'первое', '02': '', '03': '', '04': '', '05': '', '06': '', '07': '', '08': '', '09': '',
       '10': '', '11': '', '12': '', '13': '', '14': '', '15': '', '16': '', '17': '', '18': '', '19': '',
      '20': '', '21': '', '22': '', '23': '', '24': '', '25': '', '26': '', '27': ''}
print(day)