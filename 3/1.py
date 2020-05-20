# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(a, b):
    if b == 0:
        return 'Деление на ноль!'
    else:
        return a / b

def my_input(type):
    while True:
        try:
            num = int(input(f'Введите {type}: '))
            return num
        except:
            print('Введено неверное значение')

a = my_input('делимое')
b = my_input('делитель')
print(my_func(a, b))