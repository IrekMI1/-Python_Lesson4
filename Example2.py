# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите натуральное число: '))
mult_list = []
while number != 1:
    for i in range(2, number + 1):
        if number % i == 0:
            number = number // i
            mult_list.append(i)
            break
print(mult_list)