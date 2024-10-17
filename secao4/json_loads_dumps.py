# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
from typing import TypedDict  # Módulo de tipagem - Tipando o dicionário # noqa 501


class Movie(TypedDict):  # Cria uma classe e tipa as chaves do dict
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


# Salvando um json dentro de uma string com ''' '''
string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

filme: Movie = json.loads(string_json)  # filme vira instância de Movie, que agora consegue ver quais chaves filme tem # noqa 501
print(filme['characters'])  #                                 pois faz parte de atributos da classe :p # noqa 501
print(filme['year'] + 10)

json_string = json.dumps(filme, ensure_ascii=False, indent=2)  # Exibi de forma formatada # noqa 501
print(json_string)
