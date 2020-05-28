from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(10)


tl = TrafficLight()
tl.running()