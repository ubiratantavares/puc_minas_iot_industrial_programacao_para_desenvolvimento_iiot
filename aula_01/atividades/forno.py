class Forno:

    def __init__(self, setpoint, temperatura, ganho, erro):
        self.setpoint = setpoint
        self.temperatura = temperatura 
        self.ganho = ganho
        self.erro = erro

    def controlador(self):
        self.erro = self.temperatura - self.setpoint
        print(self.erro * self.ganho)

    def ajustar(self, valor):
        self.setpoint = valor

    def exibirTemp(self):
        print(self.temperatura)

    def __str__(self):
        return f'{self.setpoint}, {self.temperatura}, {self.ganho}, {self.erro}'