# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm

# from collections import namedtuple

# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )

from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'

as_espadas = Carta('A', 'Espada')

print(as_espadas._asdict()) # Exibindo minha carta em dicionário
print(as_espadas) # Minha carta como objeto
print(as_espadas[0]) # Acessando valor pelo índice
print(as_espadas.valor) # Acessando valor por .valor (NamedTuple)
print(as_espadas[1])
print(as_espadas.naipe)

print()
print(as_espadas._fields) # ._fields exibe nome dos atributos de objeto(valor, naipe) 
print(as_espadas._field_defaults) # Acessando valores padrões definidos(linha17,18)


for valor in as_espadas:
    print(valor)