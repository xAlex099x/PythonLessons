# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def degreeNumbers(a, b):
    if b == 0:
        return 1
    return a * degreeNumbers(a, b - 1)
number = int(input('Введите число: '))
degree = int(input('Введите степень: '))
print(f'{number}^{degree} = {degreeNumbers(number, degree)}')