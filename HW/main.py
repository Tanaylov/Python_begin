import os
clear = lambda: os.system('cls')
clear()

def addNote(file, list_lines):
    keys_for_note = ['Surname', 'Name', 'Tel', 'Discription']
    print('Enter:')
    note = [input(f'{keys_for_note[x]}: ') for x in range(len(keys_for_note))]
    line = dict(zip(keys_for_note, note))
    list_lines.append(line)
    with open(file, 'a') as data:
        for i in range(len(list_lines)):
            ln = ''
            for val in list_lines[i].values():
                ln += f'{val} '
            data.write(f'{ln.strip()}\n')
def printTelBook(file):
    keys_for_note = ['Surname', 'Name', 'Tel', 'Discription']
    with open(file, 'r') as data:
        for line in data:
            line = line.strip().split(' ', 3)
            line_dict = dict(zip(keys_for_note, line))
            for key, value in line_dict.items():
                print(f'{key}: {value}', end='; ')
            print()    
def searchInfo(file):
    parametr = input('Set the search parameter: ').lower()
    with open(file, 'r') as data:
        flag = True
        for line in data:
            if parametr in line.lower():
                print(line)
                return parametr
        if flag:
            print('No record with this parameter')
    return flag
def deletLine(file, lst):
    parametr = input('Enter value to delete the line: ').lower()
    flag = False
    for el in lst:
        for val in el.values():
            if parametr in val.lower():
                lst.remove(el)
                flag = True
                break
    if flag:
        with open(file, 'w') as data:
            for el in lst:
                line = ''
                for val in el.values():
                    line += f'{val} '
                data.write(f'{line.strip()}\n')
        return lst
    else:
        print('Not data to delete.')
def changeLine(file, lst):
    parametr = searchInfo(file)
    if parametr != True:
        old_val = input('Enter the value you want to change: ')
        new_val = input('Enter new value for the feild: ')
        for el in lst:
            if old_val in el.values():
                for key, val in el.items():
                    if val == old_val:
                        el[key] = new_val
                        break
            
        with open(file, 'w') as data:
            for el in lst:
                ln = ''
                for val in el.values():
                    ln += f'{val} '
                data.write(f'{ln.strip()}\n')
def deleteAll(file, lst):
    lst.clear()
    with open(file, 'w') as data:
        data.writelines(lst)
def actions(actions_list):
    print('-'*100)
    for item in actions_list.items():
        print(*item)
    action = int(input('Choose the number corresponding to your request: '))
    print('-'*100)
    return action

tel_book = 'tel_book.txt'
lines = []    
action_number = {'Add note': 1, 'Search info': 2, 'Delete line': 3,
                 'Change record': 4, 'Print telefon book': 5, 'Close': 6,
                 'Delete all': 123}

action = actions(action_number)
while action != action_number['Close']:
    if action == action_number['Add note']:
        addNote(tel_book, lines)
    elif action == action_number['Search info']:
        searchInfo(tel_book)
    elif action == action_number['Delete line']:
        deletLine(tel_book, lines)
    elif action == action_number['Change record']:
        changeLine(tel_book, lines)
    elif action == action_number['Print telefon book']:
        printTelBook(tel_book)
    elif action == action_number['Delete all']:
        deleteAll(tel_book, lines)
    action = actions(action_number)

'''
n = 0
while n != 3:
    addNote(tel_book, lines)
    print(lines)
    n += 1
printTelBook(tel_book)
searchInfo(tel_book)
searchInfo(tel_book)
deletLine(tel_book, lines)
printTelBook(tel_book)
print(lines)
changeLine(tel_book, lines)
printTelBook(tel_book)
print(lines)
'''

'''
def printTelBook(file):
    keys_for_note = ['Surname', 'Name', 'Tel', 'Discription']
    with open(file, 'r') as data:
        for line in data:
            line = line.strip().split(' ', 3)
            line_dict = dict(zip(keys_for_note, line))
            for key, value in line_dict.items():
                print(f'{key}: {value}', end='; ')
            print()

def addNote(file):
    print('Enter surname, name, tel and some discription:')
    keys_for_note = ['Surname', 'Name', 'Tel', 'Discription']
    user_note = ''
    for el in keys_for_note:
        user_note += f"{input(f'{el}: ')} "
    
    with open(file, 'a') as data:
        data.write(f'{user_note}\n')

def searchInfo(file):
    parametr = input('Set the search parameter: ').lower()
    with open(file, 'r') as data:
        flag = True
        for line in data:
            if parametr in line.lower():
                print(line)
                flag = False
                break
        if flag:
            print('No record with this parameter')
        # lines_num = len(data.readlines())
        # line = 1
        # while line != lines_num:
        #     if parametr in data.readline(line):
        #         print(data.readline(line))
        #         break
        #     print(data.readline(2))
        #     line += 1
        # else:
        #     print('No record with this parameter')

def deleteLine(file):
    parametr = input('Enter the value to delete the string: ')       
    #flag = False
    #del_line = ''
    with open(file, 'w+') as data:
        for line in data:
            if parametr not in line:
                data.write(line)
    #     lines = data.readlines()
    # if del_line != '':
    #     with open(file, 'w') as data:
    #         for line in lines:          
    #           if line.strip() != del_line:
    #                 data.write(line)
    # 

#def changeData(file):

addNote(tel_book)
printTelBook(tel_book)
print('after deleting')
deleteLine(tel_book)         
printTelBook(tel_book)

#searchInfo(tel_book)
'''