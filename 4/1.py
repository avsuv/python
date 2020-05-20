from sys import argv


def wage(h, r, p):
    return h * r + p


try:
    hours, rate, premium = float(argv[1]), float(argv[2]), float(argv[3])
    print(f'Выработка: {hours}\n'
          f'Ставка: {rate}\n'
          f'Премия: {premium}')
    print(f'З.п. сотрудника: {wage(hours, rate, premium)}')
except:
    print('Неверно введены аргументы!')