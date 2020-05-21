from sys import argv
from itertools import count, cycle
from random import randrange


def int_iter(start, finish):
    '''Итератор целых чисел в заданном промежутке'''
    new_lst = []
    for el in count(start):
        if el > finish:
            break
        else:
           new_lst.append(el)
    return new_lst

def list_iter(lst, count):
    '''Итератор, повторяющий элементы заданного списка'''
    new_lst = []
    c = 1
    for el in cycle(lst):
        if c > count:
            break
        new_lst += lst
        c += 1
    return new_lst


num_of_script = ''
try:
    num_of_script = argv[1]       # номер скрипта
    if num_of_script == 'a':             # Скрипт а)
        first_num, last_num = int(argv[2]), int(argv[3])    # первое число и последнее число последовательности
        if last_num < first_num:
            print('Неверно заданы значения')
        else:
            print(int_iter(first_num, last_num))
    elif num_of_script == 'b':           # Скрипт б)
        my_list = [el * randrange(1, 5) for el in range(1, 4)]  # Список создается рандомно
        counter = int(argv[2])                                  # После скольких итераций завершить итератор
        print(my_list)
        print(list_iter(my_list, counter))
    else:
        print('Первый аргумент либо "a", либо "b"!')
except:
    print('Введены неверные значения аргументов!')
