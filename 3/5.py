def summary(str1, pos):
    global full_sum
    for el in str1[:pos]:
        full_sum += int(el)
    return full_sum


full_sum = 0
while True:
    my_str = input('Введите числа через пробел и нажмите Enter. Для завершения, введите "*": ').split()
    if '*' in my_str:
        q_pos = my_str.index('*')
        print('Сумма:', summary(my_str, q_pos))
        break
    else:
        print('Сумма:', summary(my_str, len(my_str)))