import math


class Tanque:

    def __init__(self, altura, diametro):
        self.__altura = altura
        self.__diametro = diametro

    @property
    def altura(self):
        return self.__altura

    @property
    def diametro(self):
        return self.__diametro

    def calcular_volume(self):
        return round(math.pi * (self.diametro / 2.0) ** 2 * self.altura, 1)
