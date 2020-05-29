class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


person1 = Position('Порфирий', 'Андропов', 'Ген.дир.', {'wage': 100000, 'bonus': 50000})
print(f'Должность: {person1.position}')
print(f'{person1.get_full_name()} - {person1.get_total_income()}')
print()
person2 = Position('Глеб', 'Пугач', 'Водитель', {'wage': 40000, 'bonus': 20000})
print(f'Должность: {person2.position}')
print(f'{person2.get_full_name()} - {person2.get_total_income()}')