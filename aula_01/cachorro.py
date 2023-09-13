class Cachorro:

    def __init__(self, nome, ano, raca):
        self.nome = nome
        self.raca = raca
        self.ano = ano

    def latir(self, numero):
        print("Au " * numero)

    def pedir(self):
        print("Au au au au...")

    def imprimir(self):
        print(f'\n{self.nome} é da raça {self.raca} e nasceu no ano {self.ano}.')

    def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\nRaça: {self.raca}\n'

if __name__ == "__main__":

    c1 = Cachorro("Pitoco", 2019, "Pastor Alemão")
    c2 = Cachorro("Chave", 2019, "Pincher")
    c3 = Cachorro("Caramelo", 2022, "Vira-Lata")

    cachorros = [c1, c2, c3]

    for cachorro in cachorros:
        cachorro.imprimir()
        cachorro.latir(3)

 