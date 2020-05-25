with open('1.txt', 'w') as file:
    print('Введите данные построчно. Для выхода введите пустую строку.')
    while True:
        a = input()
        if a == '':
            break
        file.write(a + '\n')