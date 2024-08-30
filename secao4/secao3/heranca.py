# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa: # super class - Pessoa(object)
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa): # child class -Cliente(Pessoa)- recebe funções da da super class
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa): #
    cpf = 'cpf aluno'
    ...


c1 = Cliente('Luiz', 'Otávio') # criando objeto para child class cliente
c1.falar_nome_classe() # Executando função da super class Pessoa
a1 = Aluno('Maria', 'Helena') # Atributos podem entrar pela child classe e ser utilizado na super class
a1.falar_nome_classe() 
print(a1.cpf)
# help(Cliente)
