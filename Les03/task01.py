# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
number = int(input('Введите длину массива:' ))
desiredNumber = int(input('Введите искомое число:' ))
count = 0
list = []

for i in range(1,number+1):
    i = random.randint(1,number)
    list.append(i)
print(list)

for j in range(len(list)):
    if desiredNumber == list[j]:
        count += 1

print(f'Число {desiredNumber} в массиве встречаеться {count} раз(а)')