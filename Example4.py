# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import *
pow = int(input('Введите натуральную степень: '))
equation = ''
for i in range(pow, -1, -1):
    coeff = randint(0, 100)
    
    if i not in [0, 1]:
        if coeff not in [0, 1]:
            equation += f'{coeff}*x^{i} + '
        elif coeff == 1:
            equation += f'x^{i} + '
        else: continue

    elif i == 1:
        if coeff not in [0, 1]:
            equation += f'{coeff}*x + '
        elif coeff == 1:
            equation += 'x + '
        else: continue

    else:
        if coeff != 0:
            equation += f'{coeff} = 0'
        else:
            equation = equation[0:len(equation) - 2] + '= 0'

with open('file4.txt', 'w') as data:
    data.write(equation)