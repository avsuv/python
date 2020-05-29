class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Автомобиль {self.name} поехал!')

    def stop(self):
        print(f'Автомобиль {self.name} остановился!')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышена максимальная скорость 60 км/ч! Текущая скорость - {self.speed}')
        else:
            print(f'Текущая скорость - {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышена максимальная скорость 40 км/ч! Текущая скорость - {self.speed}')
        else:
            print(f'Текущая скорость - {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


tc = TownCar(58, 'Белый', 'Focus')
tc.go()
tc.show_speed()
tc.turn('налево')
tc.stop()
print()
tc1 = TownCar(80, 'Синий', 'Priora')
tc1.go()
tc1.show_speed()
print()
wc = WorkCar(30, 'Желтый', 'Belarus')
if wc.is_police == False:
    print(wc.name, '- не полицейская')
wc.go()
wc.stop()
print()
pc = PoliceCar(100, 'Черный', 'Octavia')
if pc.is_police == True:
    print(pc.name, ' - полицейская!')