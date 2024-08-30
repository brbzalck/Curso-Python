# EXIBINDO NOME COM NUMERO DO ITEM

lista = ['Maria', 'João', 'Lucas']
lista.append('Pedro') # Adicionando nome na lista

indices = range(len(lista)) # Contando a quantidade de índice da lista, e atribuindo para a VAR indices
 

print(indices) # puxa até o num 4, porque o último número nunca é incluído

for indice in indices: # para cada indice(começa com 0), em indices(vai até 3)
    print(indice, lista[indice], type(lista[indice])) # exiba o 0, lista[0], type(lista[0])