class Tanque():

    def __init__(self, obj):
        self.nivel=0
        self.agua =  obj.Canvas1.create_rectangle(0,0,300,300, fill='#333333')
        self.texto = obj.lbNivel
        self.canvas = obj.Canvas1
        self.updateTanque(self.nivel)

    def updateTanque(self,nivel):
        self.canvas.coords(self.agua,0,0,300,abs(300-nivel))
        self.texto.configure(text=str(nivel) + " L")
        print("Recebi")