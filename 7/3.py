class Cell:
    def __init__(self, n):
        self.n = n

    def __str__(self):      # переопределил метод для отображения print
        return str(self.n)

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if self.n == other.n:
            print('Разность ячеек клеток равна нулю!')
        else:
            return Cell(max(self.n, other.n) - min(self.n, other.n))    # из бОльшей вычитаем мЕньшую

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(max(self.n, other.n) // min(self.n, other.n))   # бОльшую делим на мЕньшую

    def make_order(self, i):
        if i <= 0:
            print('Неверное значение ячеек в клетке!')
        else:
            for _ in range(self.n // i):
                print('*' * i)
            if self.n % i != 0:
                print('*' * (self.n % i))

    @property
    def cell_as_asterisk(self):     # прикрутил для вывода звездочками
        print(f'{self.n}: {"*" * self.n}')


a = Cell(11)
b = Cell(18)
a.cell_as_asterisk
b.cell_as_asterisk
(a + b).cell_as_asterisk
(a - b).cell_as_asterisk
(a * b).cell_as_asterisk
(a / b).cell_as_asterisk
print()
a.make_order(3)
