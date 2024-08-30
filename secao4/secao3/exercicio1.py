# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'exercicio1.json' # Criando o caminho do arquivo

class Pessoa: # Uma classe de pessoas
    def __init__(self, nome, peso, idade, altura):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura

p1 = Pessoa('Lucas', 65, 25, 1.72)
p2 = Pessoa('Maria', 60, 22, 1.65) # Crindo objetos para classe de pessoas
p3 = Pessoa('Pedro', 35, 12, 1.05)
pessoas = [vars(p1), vars(p2), vars(p3)] # Transformando meu objeto em dict dento de uma lista

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo: # Criando o arquivo
    json.dump(pessoas, arquivo, ensure_ascii=False, indent=2) # com meus objetos desejados(pessoas)