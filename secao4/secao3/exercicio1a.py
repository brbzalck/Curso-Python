 # Importando do módulo irmão exercicio1.py, o caminho do arquivo e minha classe Pessoa
from exercicio1 import CAMINHO_ARQUIVO, Pessoa 
import json

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo: # Abrindo o arquivo 'r'
    pessoas = json.load(arquivo) # Jogando meu arquivo para VAR pessoa
    print(pessoas) # Tenho como arquivo(pessoas) uma lista de dict

    for pessoa in pessoas:
        print(pessoa)
    print()

    p1 = Pessoa(**pessoas[0]) # Desempacotando o índice 0 da minha lista de dict
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    print(vars(p1))
    print(vars(p2))
    print(vars(p3))