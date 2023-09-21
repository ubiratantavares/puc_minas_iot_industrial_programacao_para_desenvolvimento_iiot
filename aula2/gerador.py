"""
Geradores em Python

Função geradora é um tipo especial de função que não retorna um único valor, em vez disso, retorna um
objeto iterador com uma sequência de valores.

Geradores são melhores para calcular grandes quantidades de resultados onde não queremos alocar memória para todos os resultados.


"""
from time import time

class Gerador:

    def inserir(self, num, itens):
        lista = []
        for i in range(num + 1):
            for item in itens:
                lista.append(item)
        return lista
    
    def inserir2(self, num, itens):
        for i in range(num + 1):
            for item in itens:
                yield item

if __name__ == '__main__':

    gerador = Gerador()

    start = time()
    lista = gerador.inserir(100_000, [1, 2, 3])
    end = time()

    print(f'Tempo (ms): {(end - start) * 1000:.3f}')

    start = time()
    lista2 = gerador.inserir2(100_000, [1, 2, 3])
    end = time()
    
    print(f'Tempo (ms): {(end - start) * 1000:.3f}')

    # acessando os valores da lista2 usando next()
    for i in range(10):
        print(next(lista2))