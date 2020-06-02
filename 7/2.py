from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, v):
        self.v = v

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return float('{:.3f}'.format(self.v / 6.5 + 0.5))


class Suit(Clothes):
    @property
    def consumption(self):
        return 2 * self.v + 0.3


a = Coat(45)
b = Suit(15)
print(f'Общий расход ткани: {a.consumption + b.consumption}')
