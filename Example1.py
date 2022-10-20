# Вычислить число c заданной точностью d. Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import *
accuracy = float(input('Задайте точность числа пи в виде "0.00..1": '))
exponent = - log10(accuracy)
print(int(pi * 10 ** exponent) / 10 ** exponent)