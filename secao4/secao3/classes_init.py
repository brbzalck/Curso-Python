# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa: # Função dentro de classe == Método
    def __init__(self, nome, sobrenome): # Self para refenciar ao obejto criado(linha18)
        # __init__ é utilizado para inicializar os atributos da minha classe Pessoa
        self.nome = nome # Self==p1 ou p2.nome(atributos)
        self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Otávio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)