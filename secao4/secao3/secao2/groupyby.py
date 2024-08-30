# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno): # entra como parâmetro oque vem antes do key (alunos linha22)(alunos_agrupados linha23)
    return aluno['nota'] # função retorna a chave ['nota']


# Key é utilizado para personalizar a ordem dos elementos com base numa função
alunos_agrupados = sorted(alunos, key=ordena) # Ordenando a lista de alunos pelo item chave[nota]
grupos = groupby(alunos_agrupados, key=ordena) # Agrupando os alunos com a função ordena(pela nota)
# groupby me retorna um iterável, ordenado pela nota(conjunto de notas A B C) ex: A, <iteráveis>

for chave, grupo in grupos:
    print(chave) # exibindo a nota primeiro
    for aluno in grupo: # iterando meu iterável 
        print(aluno) # exibindo os itens do meu iterável


words = ['kiwi', 'apple', 'banana', 'grape', 'pear', 'orange']  # lista não ordenada de acordo com o tamanho das palavras

lista_nova = sorted(words, key=lambda x: len(x))
ordenada = groupby(lista_nova, key=lambda y: len(y))

for x, y in ordenada:
    print(x)
    for z in y:
        print(z)
