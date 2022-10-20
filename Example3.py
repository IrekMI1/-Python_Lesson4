# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers_list = list(map(int, input('Введите числа через пробел: ').split()))
unic_numbers = [i for i in numbers_list if numbers_list.count(i) == 1]
print(unic_numbers)