# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def recSum(a, b):
    if b == 0:
        return a
    return 1 + recSum(a, b - 1)
number1 = int(input('Введите число: '))
number2 = int(input('Введите число: '))
print(f'{number1} + {number2} = {recSum(number1, number2)}')