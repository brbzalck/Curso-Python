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
class Pessoa: # Super Class
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa): # Sub Class
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa): # Os objetos e atributos podem ser usados pela classe filha
    cpf = 'cpf aluno'
    ...


c1 = Cliente('Luiz', 'Otávio') # Criando um objeto na classe filha cliente
c1.falar_nome_classe() # Usando um método da super class pessoa
a1 = Aluno('Maria', 'Helena') 
a1.falar_nome_classe()
print(a1.cpf)
# help(Cliente)