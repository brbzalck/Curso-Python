# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product # Importando os métodos do módulo itertools


def print_iter(iterator): # função que recebe trecho de código
    print(*list(iterator), sep='\n') # desempacotando a list e separando por quebra de linha
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2)) # Combina independente da ordem, todas combinações possíveis
print_iter(permutations(pessoas, 2)) # Combina em ordem também, todas as combinações possíveis
print_iter(product(*camisetas)) # Combina listas de todas formas possíveis