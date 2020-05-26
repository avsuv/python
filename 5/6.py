a = []
with open('6.txt', encoding='utf-8') as file:
    for line in file:
        a.append(line.strip('\n').split(': '))

lessons = {}
for el in a:
    hours = el[1].split()
    summ = 0
    for el1 in hours:
        if el1 != '-':
            el1 = el1[:el1.index('(')]
        else:
            el1 = 0
        summ += int(el1)
    lessons[el[0]] = summ
print(lessons)