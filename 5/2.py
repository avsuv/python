a = []
try:
    with open('1.txt', 'r') as file:
        for line in file:
            a.append(line.strip().split(' '))
except:
    print('Ошибка открытия файла!')

i = 1
print(f'Количество строк в файле: {len(a)}')
for el in a:
    print(f'Количество слов в {i}-й строке: {len(el)}')
    i += 1