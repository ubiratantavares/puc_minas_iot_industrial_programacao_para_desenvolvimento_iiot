"""
Manipulando arquivos em Python

Leitura de um arquivo de texto

Escrever em um novo arquivo de texto

Abrir e adicionar uma nova informação

"""

class Arquivo:

    def __init__(self, nome):
        self.__nome = nome
        self.__arquivo = None

    @property
    def nome(self):
        return self.__nome    
  
    def abrir(self, modo):
        self.__arquivo = open(self.nome, modo)
 
    def fechar(self):
        self.__arquivo.close()

    def ler(self):
        self.abrir('r')
        texto = self.__arquivo.read()
        print(texto)
        self.fechar()

    def gravar(self, texto):
        self.abrir('w')
        self.__arquivo.write(texto + '\n')
        self.fechar()

    def atualizar(self, texto):
        self.abrir('r')
        linhas = self.__arquivo.readlines()
        self.fechar()
        linhas.append(texto + '\n')
        self.abrir('w')
        self.__arquivo.writelines(linhas)
        self.fechar()


if __name__ == '__main__':

    arq = Arquivo('lista.txt')

    #arq.gravar("Ubiratan")

    arq.ler()

    #arq.atualizar("Anna Beatriz")

    arq.atualizar("Anna Clara")

    arq.ler()


