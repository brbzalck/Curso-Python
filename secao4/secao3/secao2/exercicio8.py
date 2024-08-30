"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4, 4, 12, 54, 56, 23]

'''____________________________________________________________________________________________________________________________________'''
# LIST COMPREHESION
# mapeamento de dados soma x + y para cada x e y in zip(duas listas)
lista_soma3 = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma3) # Em vez de concatenar os dados da lista, soma com mapeamento de dados

somatoria = []
for x, y in zip(lista_a, lista_b):
    somatoria.append(x + y)

print(somatoria)
    

'''____________________________________________________________________________________________________________________________________'''
#RANGE
lista_menor = min(len(lista_a), len(lista_b)) # Pegando a minha menor lista

lista_nova = [] # criando uma lista fora do for para pegar todos os resultados
for x in range(lista_menor): # itenrando 4 vezes(tamanho da lista)(0, 1 , 2 , 3)
    lista_nova.append((lista_a[x] + lista_b[x])) # somando os indicis iniciais até os finais

print(lista_nova)

'''____________________________________________________________________________________________________________________________________'''
#RANGE LEN
lista_nova = [] # deixando a lista fora do for, para pegar todos os resultados
for x in range(len(lista_a)): # itenrando a minha menor lista
    lista_nova.append((lista_a[x] + lista_b[x])) # somando os indices iniciais até o último índice da menor lista

print(lista_nova)
'''____________________________________________________________________________________________________________________________________'''
# ENUMERATE
# lista_menor2 = min(len(lista_a), len(lista_b))

# lista_nova2 = [] #                     É USADO SOMENTE SE A LISTA B FOR A MENOR DAS LISTAS
# for i, _ in enumerate(lista_b):  #  Usando enumerate para pegar o indice e descartar o valor
#     lista_nova2.append((lista_a[i] + lista_b[i]))

# print(lista_nova2)
'''____________________________________________________________________________________________________________________________________'''
from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)] # utilizando a maior lista
print(lista_soma) #                                         e atribuindo o valor 0 para preencher os vazios