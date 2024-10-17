import json
import os

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(os.path.join(os.path.dirname(__file__), NOME_ARQUIVO))  # Caminho absoluto deste modulo aqui # noqa 501
print(CAMINHO_ABSOLUTO_ARQUIVO)  # Usando join para adicionar ao diretorio atual NOME_ARQUIVO # noqa 501

# string_json = '''
# {
#   "title": "O Senhor dos Anéis: A Sociedade do Anel",
#   "original_title": "The Lord of the Rings: The Fellowship of the Ring",
#   "is_movie": true,
#   "imdb_rating": 8.8,
#   "year": 2001,
#   "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
#   "budget": null
# }
# '''

# print(json.loads(string_json)) # Exibindo a string json em dict para ter um dict de fato(linha22) # noqa 501

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:  # Abrindo determinado caminho para leitura # noqa 501
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)  # Vou salvar o dict filme no arquivo(linha33) formatadin # noqa 501

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)  # Carregando determinado arquivo e jogando numa VAR # noqa 501
    print(filme_do_json)
