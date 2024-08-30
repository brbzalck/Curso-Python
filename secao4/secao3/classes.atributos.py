# Atributos de classe
class Pessoa:
    ano_atual = 2022 # Criando um atributo DE CLASSE que podrá ser usado em qualquer lugar da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
# Pessoa.ano_atual == Pegando um valor de fora do escopo da função, pois trata-se de um atributo da Classe 

p1 = Pessoa('João', 35) # Criando o objeto p1 com dois argumentos
p2 = Pessoa('Helena', 12) 

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento()) # Utilizando método do meu objeto p1 que faz parte da minha classe Pessoa
print(p2.get_ano_nascimento())