class Gato:

    def __init__(self, nome, cor, altura, vidas=7):
        self.nome = nome
        self.cor = cor
        self.altura = altura
        self.vidas = vidas

    def miar(self):
        print("Meow")

    def pular(self):
        self.vidas -= 1

    def dormir(self):
        self.vidas += 1

    def __str__(self):
        return f'Nome: {self.nome}, Cor: {self.cor}, Altura: {self.altura:.2f}, Vidas: {self.vidas}'
    
if __name__ == "__main__":

    g = Gato("Felix", "Preta", 0.45)

    g.miar()
    g.pular()
    g.pular()
    print(g)
    g.dormir()
    print(g)