# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

def zipper(cidade, estado): # função que recebe cidade e estado
    lista = [] # criando uma lista vazia, para uma nova lista conforme solicitado
    for x in range(len(cidade)): # para cada x(indice) nos iteráveis de cidade...   range(len(lista)) > para iterar a lista
        lista.append((cidade[x], estado[x])) # adicionando na lista uma tupla com cidade índice da vez, estado índice da vez

    return lista # fim da função com retorno da lista
    
exibir = zipper(cidade, estado) # jogando pra VAR exibir a função ziper(com os argumentos)
print(exibir)

'''______________________________________________________________________________________________________________________________________'''

['BA', 'SP', 'MG', 'RJ']
# Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def segundojeito(l1, l2): # função que recebe dois argumentos
    intervalo = min(len(l1), len(l2)) # pegando o valor mínimo dos indices de ambas listas
    return [(l2[i], l1[i]) for i in range(intervalo)]
# função retorna [listC (indiceDaVEzlista2, indiceDaVezLista1) | range(intervalo=3) > itera de 0 a 2(trez vezes)

exibir2 = segundojeito(estado, cidade) # passando as listas para minha função
print(exibir2)
'''______________________________________________________________________________________________________________________________________'''

from itertools import zip_longest # importando método do modulo que usa a maior lista preenchendo o vazio

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2))) # zip para juntar duas listas (list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE'))) # zip_longest para usar a list maior
#                              fillvalue='Msg' troca None por Msg
'''______________________________________________________________________________________________________________________________________'''


def zipper(cidade, estado): 
    lista = [] 
    i = 0 # i = 0 > i += 1 para iterar pode ser usado tbm como
    for x in cidade:  # for x in range(len(cidade)) itera a cidade
        lista.append((cidade[i], estado[i]))
        i += 1

    return lista
    
exibir = zipper(cidade, estado)
print(exibir)