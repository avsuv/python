def int_func(new_word):
    return new_word.lower().capitalize()  # Сначала все приводим к нижнему регистру, затем возвращаем с первой заглавной


latin = tuple('abcdefghijklmnopqrstuvwxyz')     # Для проверки, что введены все латинские символы

while True:
    k = True
    a = input('Введите строку: ').split()
    # Проверка на латинские символы
    for el in a:
        for symb in el:
            if symb.lower() not in latin:
                k = False
                break
    if k:
        for el in a:
            print(int_func(el), end=' ')
        break
    else:
        print('Введен не латинский символ!')