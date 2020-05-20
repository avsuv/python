# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_input(i):
    while True:
        try:
            x = int(input(f'Введите число №{i}: '))
            return x
        except:
            print('Вы ввели не число!')

def my_func(a, b, c):
    nums = [a, b, c]
    nums.remove(min(a, b, c))
    return nums[0] + nums[1]

a = my_input(1)
b = my_input(2)
c = my_input(3)

print(my_func(a, b ,c))