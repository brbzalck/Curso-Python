import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'csv_exemplo.csv'


lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'}, # Lista de dicts -> Clientes
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas) # fieldnames=para colocar os nomes da colunas no arquivo(linha14)
    # Escrevendo no meu arquivo csv em formato Dict
    escritor.writeheader() # Exibi no cabeçalho

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente) # Escrevendo cliente no arquivo csv

# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'], # Lista normal de clientes
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo: # Abrindo arquivo
#     nome_colunas = ['Nome', 'Endereço'] # Adicionando cabeçalho na unha
#     escritor = csv.writer(arquivo) # VAR que escreve no arquivo

#     escritor.writerow(nome_colunas) # Adicionando nome das colunas

#     for cliente in lista_clientes:
#         escritor.writerow(cliente) # Escrevendo cliente por cliente
