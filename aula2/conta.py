"""
Encapsulamento em Python
"""

class Conta:

    def __init__(self, valor):
        self.__valor = valor

    def imprime(self):
        print(f'Valor da conta em R$ {self.__valor:.2f}')

    def depositar(self, valor):
        self.__valor += valor
    
    def sacar(self, saque):
        if self.__valor >= saque:
            self.__valor -= saque
        

if __name__ == '__main__':
    
    conta1 = Conta(100)
    # conta1.__valor = 1_000_000.0
    conta1.imprime()
