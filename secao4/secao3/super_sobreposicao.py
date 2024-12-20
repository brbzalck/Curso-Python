# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())
'''___________________________________________________________________________________________'''
class Pessoa: # super class recebe objeto nome e iddade
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
 
 
class Estudante(Pessoa): # child class recebe herança(linha25) e adiciona mais um atributo (nota)
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade) # Herança
 
        self.nota = nota # Exclusivo da classe Estudante, a classe Pessoa não tem acesso a esse
 
estudante = Estudante("Carlos", 22, 10)
print(estudante.nome) # Carlos
print(estudante.idade) # 22
print(estudante.nota) # 10

'''___________________________________________________________________________________________'''
class A(object): # super class
    atributo_a = 'valor a'

    def __init__(self, atributo): # Classe inicia com objeto e atributo
        self.atributo = atributo

    def metodo(self): # Representando metodo da classe A
        print('A')


class B(A): # child class recebe super class A
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa): 
        super().__init__(atributo) # Classe inicia com Objeto de A, atributo e 'outra_coisa'
        self.outra_coisa = outra_coisa # Criando mais um atributo para o objeto

    def metodo(self):  # Representando metodo da classe B
        print('B')


class C(B): # child class recebe child class B e super class A
    atributo_c = 'valor c' # Automaticamente os atributos da Classe A e B existe na Classe C


# Inicializo minha classe recebendo objeto e atributos para serem repassados para as classes de cima
    def __init__(self, *args, **kwargs): 
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs) # Pegando os dados de init da classe de cima

    def metodo(self):
        # super().metodo()  # B
        # super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        A.metodo(self)
        B.metodo(self)
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
 
 
class Estudante(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade) # Herança
 
        self.nota = nota # Exclusivo da classe Estudante, a classe Pessoa não tem acesso a esse
 
estudante = Estudante("Carlos", 22, 10)
print(estudante.nome) # Carlos
print(estudante.idade) # 22
print(estudante.nota) # 10