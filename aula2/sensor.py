"""
Classe abstrata
"""

from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def update(self):
        pass

class Maquina(Sensor):

    def update(self, lista):
        for item in lista:
            print(item)


if __name__ == '__main__':

    # não podemos criar eese objeto, pois a classe é abstrata
    # s1 = Sensor()

    maq1 = Maquina()

    