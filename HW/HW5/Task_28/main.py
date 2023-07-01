'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую
сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2 = 4'''

a = 2222
b = 2

def sumAB (num1, num2):
    if num2 == 0:
        return num1
    elif num1 == 0:
        return num2
    if num1 > num2:
        if num2 == 1:
            return num1 + 1
        else:
            return sumAB(num1 = num1 + 1, num2 = num2 - 1)
    else:
        if num1 == 1:
            return num2 + 1
        else:
            return sumAB(num1 = num1 - 1, num2 = num2 + 1)

    
print(sumAB(a, b))