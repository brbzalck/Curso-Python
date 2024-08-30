# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Leão'

    def __init__(self, nome): # Segue a mesma lógica de escopo, método não acessa variável fora dela mesma(linha12)
        self.nome = nome

        variavel = 'valor' # Uma variável normal como essa, somente esse método tem acesso
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}' # A não ser que seja um atributo definido dentro do escopo geral da classe

    def executar(self, *args, **kwargs): # 
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão') # Definindo atributo(nome) para o Objeto(leao) da class Animal(class)
print(leao.nome) # Exibindo atributo definido no primeiro método
print(leao.executar('maçã')) # Exibindo Objeto com método executar(argumento)