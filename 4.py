# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input('Введите целое положительное число: '))
max = 0
while num > 0:
    if num % 10 > max:
        max = num % 10
    num //= 10
print('max = ' + str(max))