"""
Task 4 - Manipulação de arquivos
"""

from random import randint

class Arquivo:

    def __init__(self, nome_arquivo):
        self.__nome = nome_arquivo

    @property
    def nome(self):
        return self.__nome      

    def ler(self):
        try:
            lista = []
            with open(self.nome, 'r') as arquivo:
                for linha in arquivo:
                    item = linha.strip()
                    lista.append(float(item))
            return lista
        except FileNotFoundError:
            print(f"O arquivo '{self.nome}' não foi encontrado.")

    def gravar(self, lista):
        with open(self.nome, 'w') as arquivo:
            for item in lista:
                arquivo.write(str(item) + '\n')

# Sensor LIDAR (Light Detection and Ranging)
class Lidar:

    def __init__(self, nome_arquivo):
        self.__arquivo = Arquivo(nome_arquivo)
        self.__distancia = self.__arquivo.ler()
     
    def update(self, tempo):
        """
        este método recebe o tempo em nanosegundos
        """
        velocidade = 3.0e8 # velocidade da luz em metros/segundos
        tempo_s = 1.0e-9 * tempo # tempo em segundos
        dist = round(velocidade * tempo_s, 1) # distancia em metros)
        self.__distancia.append(dist)

    def soma(self):
        return sum(self.__distancia)
    
    def quantidade(self):
        return len(self.__distancia)

    def media(self):
        return self.soma() / self.quantidade()

    def gravar(self):
        self.__arquivo.gravar(self.__distancia)
        print(f"O arquivo '{self.__arquivo.nome} foi gravado com sucesso.")


if __name__ == "__main__":

    lidar = Lidar("atividade1/medicoes.txt")    

    print(f"Soma das distâncias: {lidar.soma():.2f}")
    print(f"Quantidade de distâncias: {lidar.quantidade()}")
    print(f"Média das distâncias: {lidar.media():.2f}")

    # adicionar mais 10 medições aleatórias entre 0 e 5 ns
    for _ in range(0, 10):
        lidar.update(randint(0, 5))      
    
    # gravar as atualizações
    lidar.gravar()

    lidar = Lidar("atividade1/medicoes.txt")    
    
    print(f"Soma das distâncias: {lidar.soma():.2f}")
    print(f"Quantidade de distâncias: {lidar.quantidade()}")
    print(f"Média das distâncias: {lidar.media():.2f}")
    