"""
Polimorfismo - Substituição do método
"""

class Poligono:

    def __init__(self):
        self.__area = 0

    def calcArea(self):
        return 0.0  
    

class Quadrado(Poligono):

    def __init__(self, lado):
        super().__init__()
        self.__lado = lado

    def calcArea(self):
        return self.__lado ** 2.0
    

if __name__ == '__main__':

    quad1 = Quadrado(10)
    print(quad1.calcArea())