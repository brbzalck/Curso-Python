# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
import string
from datetime import datetime
from pathlib import Path


CAMINHO_ARQUIVO = Path(__file__).parent / 'string_template.txt' # Criando caminho 

# with open(CAMINHO_ARQUIVO, 'w') as arquivo: # Criando meu arquivo
#     arquivo.write('string_template.txt')

locale.setlocale(locale.LC_ALL, '') # Setando a região que estou

def converte_num_br(num: float) -> str:
    brl = 'R$' + locale.currency(num, symbol=False, grouping=True) # Retorna a moeda em str sem simbolos e agrupados
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_num_br(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto) # Classe template recebe texto que vai ser formatado(argumento=texto) (self=template)
    print(template.substitute(dados)) # Usando método no objeto instânciado de Template substitute(argumento=dados)