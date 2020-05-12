# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 8
b = 45
c = 10
print('a = ' + str(a))
print('b + c = ' + str(b + c))
print('b - c = ' + str(b - c))
print('b / c = ' + str(b / c))
print('b * c = ' + str(b * c))
print('b % (c + a) = ' + str(b % (c + a)))
print('b^(c - a) = ' + str(b ** (c - a)))

surname = input('Введите Фамилию: ')
name = input('Введите Имя: ')
age = int(input('Введите возраст: '))
height = int(input('Введите вес: '))
length = int(input('Введите рост: '))
print(surname + ' ' + name + ' ' + str(age) + ' ' + str(height) + ' ' + str(length))
