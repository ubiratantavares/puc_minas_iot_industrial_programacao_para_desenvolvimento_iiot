"""
Task 2 - Herança
"""

class Planta:

    def __init__(self, nomePlanta, cidadePlanta):
        self.__nomePlanta = nomePlanta
        self.__cidadePlanta = cidadePlanta

    @property
    def nomePlanta(self):
        return self.__nomePlanta
    
    @property
    def cidadePlanta(self):
        return self.__cidadePlanta
    
class Maquina(Planta):

    def __init__(self, nomePlanta, cidadePlanta, nomeMaquina, temperatura, pressao):
        super().__init__(nomePlanta, cidadePlanta)
        self.__nomeMaquina = nomeMaquina
        self.__temperatura = temperatura
        self.__pressao = pressao

    @property
    def nomeMaquina(self):
        return self.__nomeMaquina
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @property
    def pressao(self):
        return self.__pressao
    
    def getTemperaturaC(self):
        print(f'Temperatura {self.temperatura:.2f} graus Celsius')

    def getTemperaturaF(self):
        print(f'Temperatura {(9 / 5 * self.temperatura + 32):.2f} graus Fahrenheit')

    def getPressao(self):
        print(f'A pressão interna do compressor: {self.pressao:.2f} bar')
    

if __name__ == "__main__":

    maquina1 = Maquina('Laminadora de alumínio', 'Belo Horizonte-MG', 'Forno 1', 100, 2)
    maquina1.getTemperaturaC()
    maquina1.getTemperaturaF()
    maquina1.getPressao()
    print(f'{maquina1.nomePlanta}')