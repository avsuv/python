import json

a = []
with open('7.txt', encoding='utf-8') as file:
    for line in file:
        a.append(line.strip('\n').split('\t'))
print(a)

firms = {}  # Фирмы с прибылью
total_profit = 0    # общая прибыль без отрицательных значений
i = 0   # Кол-во фирм с положительной прибылью
for el in a:
    profit = int(el[2]) - int(el[3])
    firms[el[0]] = profit
    if profit > 0:
        i += 1
        total_profit += profit
a.clear()   # Запишем в тот же список все
a.append(firms)
a.append(dict(Average_profit=f'{(total_profit/i):.2f}'))
with open('7.json', 'w', encoding='utf-8') as file:
    for el in a:
        json.dump(el, file)