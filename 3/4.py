def my_input(i, my_type):
    while True:
        try:
            a = my_type(input(f'Введите {i} число: '))
            return a
        except:
            print('Вы ввели не число!')

def my_func1(x, y):     # Первый способ
    return x ** y

def my_func2(x, y):     # Второй способ
    for _ in range(1, abs(y)):
        x *= x
    return 1 / x

a = -1
b = 1
while a < 0:
    a = my_input('действительное положительное', float)
while b > 0:
    b = my_input('целое отрицательное', int)
print(my_func1(a, b))
print(my_func2(a, b))