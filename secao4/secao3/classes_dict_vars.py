# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35} # Passando um dict como atributos do meu objeto
p1 = Pessoa(**dados) # Desempacotando o dict na classe Pessoa, e criando um novo objeto
#p1 = Pessoa(nome='João', idade=35) (EXEMPLO DE COMO FUNCIONA O DESEMPACOTAMENTO)

# p1.nome = 'EITA'
# print(p1.idade)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)


print(vars(p1)) # Função para exibir meu objeto em dict
print(p1.nome) # Exibindo atributo(nome) do meu objeto(p1)
# ISSO TUDO POR MEIO DO DESEMPACOTAMENTO DO DICT NA CLASSE PESSOA