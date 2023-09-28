from task1 import Tanque

if __name__ == '__main__':

    niveis = [0.2, 0.6, 1.1]

    tanque1 = Tanque(diametro=1.2, altura=3.0)

    for nivel in niveis:
        print("Tanque 1")
        tanque1.update(50, 10, nivel)
        tanque1.gerarRelatorio()
        tanque1.getStatus()

    tanque2 = Tanque()

    for nivel in niveis:
        print("Tanque 2")
        tanque2.update(50, 10, nivel)
        tanque2.gerarRelatorio()
        tanque2.getStatus()