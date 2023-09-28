"""
Task 3 - Encapsulamento e polimorfismo
"""

class Medidor:

    def __init__(self, *args):
        lista = []
        for item in args:
            lista.append(str(item))
        del lista[0]
        concatenado = ' '.join(lista)
        self.__nome = concatenado
        self.__valor = 0

    def setNome(self, *args):
        lista = []
        for item in args:
            lista.append(str(item))
        del lista[0]
        concatenado = ' '.join(lista)
        self.__nome = concatenado

    @property
    def valor(self):
        return self.__valor
    
    @property
    def nome(self):
        return self.__nome

    def getNome(self):
        return f"Nome do termopar: {self.nome}"
    
    def setValor(self, valor):
        self.__valor = valor

    def getValor(self):
        return self.valor
    
class Termopar(Medidor):

    def __init__(self, *args):
        super().__init__(self, *args)    

    def getValor(self):
        return f"Medição no termopar: {self.valor} ºC"
    

if __name__ == "__main__":
    termopar = Termopar("Termopar", "Tipo J", "Flexível", "6mm 2m", "View", "Tech")
    termopar.setValor(370)
    print(termopar.getNome())
    print(termopar.getValor())


