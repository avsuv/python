def my_input(i, my_type):
    while True:
        try:
            x = my_type(input(f'Введите {i} число: '))
            return x
        except:
            print('Вы ввели не число!')

def my_func1(a, b):     # Первый способ
    return a ** b

def my_func2(a, b):     # Второй способ
    for _ in range(1, abs(b)):
        a *= a
    return 1 / a

a = -1
b = 1
while a < 0:
    a = my_input('действительное положительное', float)
while b > 0:
    b = my_input('целое отрицательное', int)
print(my_func1(a, b))
print(my_func2(a, b))