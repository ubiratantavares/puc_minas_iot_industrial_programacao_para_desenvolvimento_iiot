from datetime import date

class PlantaIndustrial:

    def __init__(self):
        self.lista = []

    def adicionar_sensor(self, sensor):
        self.lista.append(sensor)

    def imprimir_relatorio(self):
        print("=======================")
        print("****** Relatório ******")
        print(f"Data: {date.today()}")
        # print(f"Data: {date.today().strftime('%d/%m')}")
        for sensor in self.lista:
            print(sensor)
        print("***********************")
        print("=======================")


from sensor import SensorPressao

if __name__ == "__main__":
    s1 = SensorPressao("Sensor1", 2)
    s2 = SensorPressao("Sensor2", 10)
    s3 = SensorPressao("Sensor3", 1)
    s4 = SensorPressao("Sensor4", 2)
    s5 = SensorPressao("Sensor5", 5)
    s6 = SensorPressao("Sensor6", 1)
    s7 = SensorPressao("Sensor7", 2)
    s8 = SensorPressao("Sensor8", 0)
    s9 = SensorPressao("Sensor9", 2)
    s10 = SensorPressao("Sensor10", 9)

    pi = PlantaIndustrial()

    pi.adicionar_sensor(s1)
    pi.adicionar_sensor(s2)
    pi.adicionar_sensor(s3)
    pi.adicionar_sensor(s4)
    pi.adicionar_sensor(s5)
    pi.adicionar_sensor(s6)
    pi.adicionar_sensor(s7)
    pi.adicionar_sensor(s8)
    pi.adicionar_sensor(s9)
    pi.adicionar_sensor(s10)
    pi.imprimir_relatorio()
