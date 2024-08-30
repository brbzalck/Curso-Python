"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         0   1   2   3   4   5
lista1 = [10, 20, 30, 40, 1, 2, 3, 4]
lista2 = ['a', 'b', 'c', 'd']
lista_nova = lista1 + lista2 # Juntando listas com concatenação +
lista_nova[2] = 300 # trocando o valor do item 2 da lista
del lista_nova[4] # deletando o valor do item 4 da lista
del lista_nova[-1] # Utilizado para remover o último item da lista(pois o último SEMPRE vai ter -1 atribuido)
lista_nova.append(50) # MÉTODO Utlizado para adicionar valor ao final da lista
lista_nova.pop() # MÉTODO Utilizado para remover o ultimo item da lista
lista_nova.append(30)
teste = lista_nova.pop() # ALEM DE REMOVER, ELA GUARDA O VALOR REMOVIDO PODENDO SER UTILIZADO.... = 30
print(teste)
lista_nova.append(50)
lista_nova.insert(6, 'Lucas') # Adiciona um item no índice escolhido
lista_nova = lista_nova + lista2 # Juntando listas com concatenação
lista_x = ['Barbosa', 'Dev']
lista_nova.extend(lista_x) # ADICIONANDO A LISTA_X EM LISTA NOVA(método de concatenação)
removido = lista_nova.pop(5) # MÉTODO pop(x item) para remover item especifico
# lista_nova.clear() # SERVE PARA LIMPAR A LISTA

print(lista_nova, 'Removido,', removido)