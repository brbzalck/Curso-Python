import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# abrindo o arquivo e fechando com with open ('definindo nome do arquivo', 'w=escrever', formatação de acentos)
with open('salvandoArquivo', 'w', encoding='utf8') as arquivo: # 
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2) 
# json.dump(definição de arquivo)(oque tem no arquivo, o arquivo(salvandoArquivo), formatação, separando por 2(identação))   
'''____________________________________________________________________________________________________________________________________________________'''
# lendo o arquivo com with open 'r', formatação para acentos, as arquivo para chamar isso tudo
with open('salvandoArquivo', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo) # carregando os dados do arquivo para VAR pessoa

print(pessoa)