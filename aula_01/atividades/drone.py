class Drone:

    marca = 'XPTO'

    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def consultar(self):
        return self.preco * 5.0
    
if __name__ == "__main__":

    thunder = Drone('Thunder', 3000.00)
    print(thunder.marca)
    print(Drone.marca)