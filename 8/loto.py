import random


class GenerateCard:
    def __init__(self, is_comp=True):
        self.card = self.create_card()     # сразу запускаем функцию генерации карточки с номерами
        self.is_comp = is_comp      # определяет тип игрока
        self.count = 0          # счетчик вычеркнутых номеров

    def __str__(self):
        if self.is_comp:
            title = '-- Карточка компьютера ---\n'
        else:
            title = '------ Ваша карточка -----\n'
        card_prnt = title
        for line in self.card:
            for el in line:
                card_prnt += str(el).ljust(3)   # выравниваем цифры по строке
            card_prnt += '\n'
        card_prnt += '--------------------------'
        return card_prnt

    @staticmethod       # что-то ругался на атрибуты по умолчанию - решил обернуть в staticmethod
    def create_card():
        numbers = [num for num in random.sample(range(1, 91), 15)]  # генерируем 15 чисел
        numbers.sort()          # сортируем их
        card = [numbers[:5], numbers[5:10], numbers[10:]]   # делим на три группы по 5 чисел
        for el in card:
            for _ in range(4):
                el.insert(random.randint(0, len(el)), ' ')  # докидываем по 4 пробела в случайные позиции в эти 3 группы
        return card

    def check_keg(self, keg):
        for line in self.card:
            for el in line:
                if str(el) == str(keg):
                    pos = line.index(keg)   # ищем позицию номера, совпавшего с номером бочонка
                    line.insert(pos, '-')   # ставим крести в этом месте, сдвигая последующие элементы
                    line.pop(pos + 1)       # удаляем элемент на позиции номера бочонка
                    self.count += 1
                    if self.count == 15:    # условие победы
                        if self.is_comp:
                            print('Игра окончена! Победил компьютер!')
                            exit()
                        else:
                            print('Игра окончена! Победил игрок!')
                            exit()
                    return True
        return False


class Game:
    def __init__(self, p_1, p_2):
        self.p_1 = p_1  # Игрок 1
        self.p_2 = p_2  # Игрок 2
        self.kegs = [el for el in range(1, 91)] # генерерием номера бочонков

    def next_keg(self):
        return self.kegs.pop(random.randint(0, len(self.kegs)-1))   # вытаскиваем случайный бочонок

    def play(self):
        while len(self.kegs) != 0:
            keg = self.next_keg()
            print(f'Номер бочонка: {keg}. Осталось: {len(self.kegs)}')
            print(player)
            print(computer)
            if len(self.kegs) == 0:
                print('Игра окончена! Ничья!')  # редко, но бывает...
            choise = input('Хотите зачеркнуть? (y/n): ')
            if choise == 'y':
                if not player.check_keg(keg):   # если этого номера не оказалось в карточке
                    print('Вы проиграли!')
                    break
            elif choise == 'n':
                if player.check_keg(keg):       # если номер оказался в карточке, но не вычеркнули
                    print('Вы проиграли!')
                    break
            computer.check_keg(keg)  # у компьютера просто преверяем наличие номера в карточке и вычеркиваем при наличии


player = GenerateCard(False)
computer = GenerateCard()
new_game = Game(player, computer)
new_game.play()
