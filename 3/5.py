def summary(str1):
    global full_sum
    for el in str1:
        full_sum += el
    return full_sum


full_sum = 0    # Сумма аргументов
while True:
    my_str = input('Введите числа через пробел и нажмите Enter. Для завершения, введите "*": ').split()
    if '*' in my_str:
        q_pos = my_str.index('*')   # Узнаем позицию спецсимвола
        my_str = list(map(float, my_str[:q_pos]))   # Переводим значения до спецсимвола во float
        print('Сумма:', summary(my_str))
        break
    else:
        try:
            my_str = list(map(float, my_str))   # Если введено не число и не спецсимвол, обрабатываем ошибку
            print('Сумма:', summary(my_str))
        except:
            print('При вводе допущена ошибка!')