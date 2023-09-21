"""
Atividades de Orientação a Objetos
"""

class Sensor:

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor(self):
        return self.__valor

    def ler(self):
        print(f'Leitura atual do sensor {self.__nome}: {self.__valor:.2f}')
    
class SensorPressao(Sensor):

    def __init__(self, nome, valor):
        super().__init__(nome, valor)  

    def ler(self):
       print(f'Leitura atual do sensor de pressão {self.nome}: {self.valor:.2f}')

class SensorVazao(Sensor):

    def __init__(self, nome, valor):
        super().__init__(nome, valor)  

    def ler(self):
       print(f'Leitura atual do sensor de vazão {self.nome}: {self.valor:.2f}')


if __name__ == '__main__':

    s1 = SensorPressao('s1', 10)
    s2 = SensorVazao('s2', 100)
    s1.ler()
    s2.ler()

