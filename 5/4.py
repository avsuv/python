numbers = []
with open('2.txt') as file:
    for line in file:
        numbers.append(line.strip().split(' '))

for el in numbers:
    if el[0] == 'One':
        el[0] = 'Один'
    elif el[0] == 'Two':
        el[0] = 'Два'
    elif el[0] == 'Three':
        el[0] = 'Три'
    elif el[0] == 'Four':
        el[0] = 'Четыре'

with open('2_new.txt', 'w', encoding='utf-8') as file:
    for line in numbers:
        a = ' '.join(line)
        file.write(a + '\n')