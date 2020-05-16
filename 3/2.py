# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def info(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)

people = {'Name': '', 'Surname': '', 'Birth year': '', 'City': '', 'Email': '', 'Phone': ''}

for key in people.keys():
    if key == 'Birth year' or key == 'Phone':
        while True:
            try:
                people[key] = int(input(f'{key}: '))
                break
            except:
                print('Введите число!')
    else:
        people[key] = input(f'{key}: ')

info(name=people['Name'], surname=people['Surname'], year=people['Birth year'], city=people['City'],
     email=people['Email'], phone=people['Phone'])
