"""
Polimorfismo - Sobrecarga do método
"""

class Resistor:

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor(self):
        return self.__valor
    
    def __str__(self):
        return f'{self.nome} = {self.valor:.1f} Ohm.'
    
class ResistorEquivalente:

    def __init__(self, *args):
        self.__args = args
        self.__valor = 0.0

    def serie(self):
        for item in self.__args:
            self.__valor += item.valor

    def paralelo(self):
        for item in self.__args:
            self.__valor += 1 / item.valor
        self.__valor = 1 / self.__valor
    
    def __str__(self):
        return f'Resistor Equivalente: {self.__valor:.1f} Ohm.'
    
if __name__ == '__main__':

    r1 = Resistor('R1', 10)
    print(r1)
    r2 = Resistor('R2', 20)
    print(r2)
    r3 = Resistor('R2', 20)
    print(r3)

    req1 = ResistorEquivalente(r1, r2, r3)
    req1.serie()
    print(req1)

    req2 = ResistorEquivalente(r2, r3)
    req2.paralelo()
    print(req2)

    