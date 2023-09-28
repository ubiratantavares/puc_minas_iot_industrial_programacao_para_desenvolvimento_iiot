"""
Task 1 - Classe e instâncias
"""

from math import pi

class Tanque:

    def __init__(self, diametro=1.0, altura=1.0):
        """
        diametro e altura em metros
        """
        if diametro > 0:
            self.__diametro = diametro
        else:
            raise ValueError("Valor do diâmetro é inválido.")
        
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("Valor da altura é inválido.")  
        self.__vazao1 = 0.0
        self.__vazao2 = 0.0
        self.__nivel1 = 0.0
        self.__volume = 0.0

    @property
    def diametro(self):
        return self.__diametro    
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def vazao1(self):
        return self.__vazao1
    
    @property
    def vazao2(self):
        return self.__vazao2
    
    @property
    def nivel1(self):
        return self.__nivel1
    
    @property
    def volume(self):
        return self.__volume
    
    def raio(self):
        return self.diametro/2
    
    def getArea(self):
        return pi * self.raio() ** 2
    
    def getVolumeTotal(self):
        """
        retorna o volume total do cilindro em litros
        """
        return 1000 * self.getArea() * self.altura
    
    def getVolume(self):
        return 1000 * self.getArea() * self.nivel1
    
    def getNivel(self):
        """
        Retorna o valor do nível em percentual (valor entre 0 e 100%)
        """
        return 100 * self.nivel1 / self.altura

    def getStatus(self):
        status = ["Baixo", "Médio", "Alto"]
        if self.getNivel() <= 30:
            print(f"Status: {status[0]}\n")
        elif self.getNivel() <= 60:
            print(f"Status: {status[1]}\n")
        else:
            print(f"Status: {status[2]}\n")  
    
    def update(self, vazao1, vazao2, nivel):
        """
        - a medição da vazão de entrada em litros/min: vazao1
        - a medição da vazão de saída em litros/min: vazao2
        - a medição do nível de líquido no tanque em metros: nivel1
        """
        self.__vazao1 = vazao1
        self.__vazao2 = vazao2
        self.__nivel1 = nivel
        self.__volume = self.getVolume()

    def gerarRelatorio(self):
        print(f"Vazao de entrada: {self.vazao1:.2f} L/min")
        print(f"Vazao de saída: {self.vazao2:.2f} L/min")
        print(f"Nível: {self.nivel1:.2f} m") 
        print(f"Volume: {self.volume:.2f} L")





class Tanque2:
    """
    Elaboração da classe Tanque para atender o cliente que deseja desenvolver um sistema IOT
    Industrial na empresa PHJ Tech.
    No Tanque foram instalados três sensores:
    - 2 sensores de vazão (L/min)
    - 1 sensor ultrassônico para a medição do nível de água (m)
    """   
    def __init__(self, diametro=1.0, altura=1.0, nivel=0.0):
        """
        diametro e altura em metros
        """
        if diametro > 0:
            self.__diametro = diametro
        else:
            raise ValueError("Valor do diâmetro é inválido.")
        
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("Valor da altura é inválido.")
        
        if (nivel >= 0) and (nivel <= self.altura):
            self.__nivel = nivel
        else:
            raise ValueError("Valor do nivel é inválido.")

    @property
    def diametro(self):
        return self.__diametro    
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def vazao1(self):
        return self.__vazao1
    
    @property
    def vazao2(self):
        return self.__vazao2
    
    @property
    def nivel(self):
        return self.__nivel
    
    def raio(self):
        return self.diametro/2
    
    def area(self):
        return pi * self.raio() ** 2
    
    def volume(self):
        """
        retorna o volume total do cilindro em litros
        """
        return 1000 * self.area() * self.altura
    
    def getNivel(self):
        """
        Retorna o valor do nível em percentual (valor entre 0 e 100%)
        """
        return 100 * self.nivel / self.altura

    def getStatus(self):
        """
        retorna o status do nível do tanque
        """
        status = ["Baixo", "Médio", "Alto"]
        if self.getNivel() <= 30:
            return status[0]
        elif self.getNivel() <= 60:
            return status[1]
        return status[2]
    
    def getSituacao(self):
        if self.getNivel() == 0:
            return "Tanque vazio"
        if self.getNivel() == 100:
            return "Tanque completamente cheio"
        return "Tanque " + self.getStatus()
    
    def getVolume(self):
        """
        retorna o volume ocupado em litros
        """
        return 1000 * self.area() * self.nivel   
    
    def update(self, nivel):
        self.nivel = nivel

    def gerarRelatorio(self):
        print(f"Nível: {self.nivel:.2f} m ({self.getNivel():.2f} % da altura - Status: {self.getSituacao()})")
        print(f"Altura: {self.altura:.2f} m")
        print(f"Área da seção transversal: {self.area():.2f} m2")
        print(f"Volume total: {self.volume():.2f} L")        
        print(f"Volume ocupado: {self.getVolume():.2f} L")
        print(f"Volume livre: {(self.volume() - self.getVolume()):.2f} L\n")




class Tanque3:
    """
    Elaboração da classe Tanque para atender o cliente que deseja desenvolver um sistema IOT
    Industrial na empresa PHJ Tech.
    No Tanque foram instalados três sensores:
    - 2 sensores de vazão (L/min)
    - 1 sensor ultrassônico para a medição do nível de água (m)
    """   
    def __init__(self, diametro=1.0, altura=1.0, nivel=0.0):
        """
        diametro e altura em metros
        """
        if diametro > 0:
            self.__diametro = diametro
        else:
            raise ValueError("Valor do diâmetro é inválido.")
        
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("Valor da altura é inválido.")
        
        if (nivel >= 0) and (nivel <= self.altura):
            self.__nivel = nivel
        else:
            raise ValueError("Valor do nivel é inválido.")

    @property
    def diametro(self):
        return self.__diametro    
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def vazao1(self):
        return self.__vazao1
    
    @property
    def vazao2(self):
        return self.__vazao2
    
    @property    
    def nivel(self):
        return self.__nivel
    
    def raio(self):
        return self.diametro/2
    
    def area(self):
        return pi * self.raio() ** 2
    
    def volume(self):
        """
        retorna o volume total do cilindro em litros
        """
        return 1000 * self.area() * self.altura
    
    def getNivel(self):
        """
        Retorna o valor do nível em percentual (valor entre 0 e 100%)
        """
        return 100 * self.nivel / self.altura

    def getStatus(self):
        """
        retorna o status do nível do tanque
        """
        status = ["Baixo", "Médio", "Alto"]
        if self.getNivel() <= 30:
            return status[0]
        elif self.getNivel() <= 60:
            return status[1]
        return status[2]
    
    def getVolume(self):
        """
        retorna o volume ocupado em litros
        """
        return 1000 * self.area() * self.nivel
    
    def taxa_de_variacao_do_nivel_no_tempo(self, vazao1, vazao2):
        """
        retorna a taxa de variação do nível do líquido no tanque em metros por minuto
        """

        # princípio da continuidade: a vazão de entrada deve ser igual à vazão de saída para que o nível do líquido no tanque permaneça constante, tal que:

        # Q1 - Q2 = A * dh/dt, onde:

        # Q1: vazão de entrada em litros por minuto
        # Q2: vazão de saída em litros por minuto
        # A: a área da seção transversal do tanque em metros quadrados
        # dh/dt: taxa de variação do nível do líquido no tanque em metros por minuto
        
        return (0.001 * (vazao1 - vazao2)) / self.area() 
    
    def update(self, vazao1, vazao2, tempo):
        novo_nivel = self.taxa_de_variacao_do_nivel_no_tempo(vazao1, vazao2) * tempo + self.nivel
        if (novo_nivel > 0) and (novo_nivel < self.altura):
            self.__nivel = novo_nivel
        if novo_nivel <= 0:
            self.__nivel = 0.0
        if novo_nivel >= self.altura:
            self.__nivel = self.altura

    def getSituacao(self):
        if self.getNivel() == 0:
            return "Tanque vazio"
        if self.getNivel() == 100:
            return "Tanque completamente cheio"
        return "Tanque " + self.getStatus()

    def gerarRelatorio(self):
        print(f"Nível: {self.nivel:.2f} m ({self.getNivel():.2f} % da altura - Situação: {self.getSituacao()})")
        print(f"Altura: {self.altura:.2f} m")
        print(f"Área da seção transversal: {self.area():.2f} m2")
        print(f"Volume total: {self.volume():.2f} L")        
        print(f"Volume ocupado: {self.getVolume():.2f} L")
        print(f"Volume livre: {(self.volume() - self.getVolume()):.2f} L\n")