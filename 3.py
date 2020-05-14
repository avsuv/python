# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

while True:
    try:
        month = int(input('Введите порядковый номер месяца:'))
        if (month < 1) or (month > 12):
            print('Месяцев всего 12!')
        else:
            break
    except:
        print('Вы ввели неверное значение! Попробуйте ещё!')

# Через list
# seasons = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]   # Зима, Весна, Лето, Осень
# for months in seasons:
#     for i in months:
#         if i == month:
#             position = seasons.index(months)
#             break
# if position == 0:
#     print('Зима')
# if position == 1:
#     print('Весна')
# if position == 2:
#     print('Лето')
# if position == 3:
#     print('Осень')

# Через dict
seasons = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for el in seasons:
    if month in seasons.get(el):
        print(el)
        break
