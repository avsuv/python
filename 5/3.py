staff = []
try:
    with open('1.txt', encoding='utf-8') as file:
        for line in file:
            staff.append(line.strip().split(' '))
except:
    print('Ошибка открытия файла!')

# Ищем сотрудников с з\п меньше 20000
staff_min = [el[0] for el in staff if float(el[1]) < 20000]
print('Сотрудники с зарплатой менее 20тыс.:')
for i, el in enumerate(staff_min):
    print(f'{i+1}.{el}')

# Ищем средню з\п всех сотрудников
ave_salary = 0
for el in staff:
    ave_salary += float(el[1])
print(f'Средняя зарплата всех сотрудников: {ave_salary / len(staff)}')