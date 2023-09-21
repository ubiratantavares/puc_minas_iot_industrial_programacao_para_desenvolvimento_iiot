class SensorPressao:

    def __init__(self, nome, pressao):
        self.nome = nome
        self.pressao = pressao if (pressao >= 0 and pressao <= 10) else 0

    def get_nome(self):
        return self.nome
    
    def get_pressao(self):
        return self.pressao
    
    def status(self):
        if self.pressao < 3:
            return  "Ok"
        elif self.pressao <= 8:
            return "Alerta"
        return "Emergência"
    
    def __str__(self):
        return f'{self.get_nome()}: {self.status()}'