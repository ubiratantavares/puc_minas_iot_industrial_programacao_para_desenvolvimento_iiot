class Pessoa:

    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

class Funcionario(Pessoa):

    def __init__(self, nome, cpf, endereco, matricula):
        super().__init(nome, cpf, endereco)
        self.matricula = matricula

class Gerente(Funcionario):

    def __init__(self, nome, cpf, endereco, matricula, setor):
        super().__init__(nome, cpf, endereco, matricula)
        self.setor = setor  
    
class Operador(Funcionario):

    def __init__(self, nome, cpf, endereco, matricula, maquina):
        super().__init__(nome, cpf, matricula, endereco)
        self.maquina = maquina


