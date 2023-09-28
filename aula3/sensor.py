from  abc import ABC, abstractmethod   

class Sensor(ABC):

    @abstractmethod
    def update(self, lista):
        pass
    
class Maquina(Sensor):

    def update(self, lista):
        print("---Atualização---")
        for item in lista:
            print("Valor = ", item)

if __name__ == '__main__':

    maquina1 = Maquina()
    maquina1.update(range(0, 6))