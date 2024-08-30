# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

# EM SUMA CLASSMETHOD, CRIA UM OBJETO COM ALGUM MÉTODO(LÓGICA) ESPECÍFICA

class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade): # Método para criar Objeto e atributos da classe pessoa
        self.nome = nome
        self.idade = idade

# @DECORATOR EXECUTA O MÉTODO-FUNÇÃO

    @classmethod # Método exclusivo da classe
    def metodo_de_classe(cls): # Onde se refencia por meio de cls(class) em vez de self(objeto)
        print('Hey') # O método da classe não tem acesso aos dados dos Objetos(self)

    @classmethod
    def criar_com_50_anos(cls, nome): # Mesma coisa do que criar na mão(linha25, 27)
        return cls(nome, 50)
    # retorna Pessoa(Helena, 50) == p2

    @classmethod # É uma fabrica de objetos para lógicas especificas, nesse caso de pessoas anônimas
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()