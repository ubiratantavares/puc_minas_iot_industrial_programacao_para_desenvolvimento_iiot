class Maquina:

    def __init__(self, nome, tamanho, peso):
        self.nome = nome
        self.tamanho = tamanho
        self.peso = peso
        self.status = False  # True: Ligado e False: Desligado
    
    def ligar(self):
        if not self.status:
            self.status = True
    
    def desligar(self):
        if self.status: 
            self.status = False
   
    def get_status(self):
        return self.status

    def __str__(self):
        if self.status:
            return f'{self.nome}: Ligado'
        return f'{self.nome}: Desligado'
    
    
if __name__ == "__main__":
    
    maq = Maquina('Gerador-1', 2.5, 200)
    print(maq)
    maq.ligar()
    print(maq)    
    maq.desligar()
    print(maq)   