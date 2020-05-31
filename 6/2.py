class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__const_m = 25       # Масса асфальта для покрытия 1кв.м. дороги, толщиной 1 см

    def mass(self, depth):
        m = self._length * self._width * self.__const_m * depth
        return m


a = Road(2, 1)
print(f'Масса асфальта: {a.mass(5)} тонн')