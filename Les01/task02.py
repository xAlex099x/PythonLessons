# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

number = int(input('Введите количество журавликов (кратное 3):' ))
if number % 6 == 0:
    petia = number/3/2
    katia = number - number/3
    sergey = number/3/2
    print(f'Петя сделал {int(petia)} - Катя сделала {int(katia)} - Сергей сделал {int(sergey)}')
else: print('Не верное число')