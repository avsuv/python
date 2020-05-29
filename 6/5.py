class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки...')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} - запуск отрисовки...')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}: запуск отрисовки...')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}... запуск отрисовки...')


a = Pen('Ручка')
b = Pencil('Карандаш')
c = Handle('Маркер')
a.draw()
b.draw()
c.draw()