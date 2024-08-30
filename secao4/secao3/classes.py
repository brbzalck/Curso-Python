# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))


class Pessoa: # Definindo uma classe chamada pessoa
    ...


p1 = Pessoa() # Criando uma instância da classe Pessoa
p1.nome = 'Luiz'
p1.sobrenome = 'Otávio' # Adicionando atributos para minha instância p1

p2 = Pessoa()
p1.nome = 'Lucas'
p2.nome = 'Barbosa'

print(p1.nome) 
print(p1.sobrenome)

print(p2.nome) # Acessando um atributo do objeto p2 da classe Pessoa
print(p2.sobrenome)