lista = ['Maria','Helena', 'Luiz']
lista.append("Lucio")

for indice in enumerate(lista): # FUNÇÃO para enumerar a lista retornando uma tuple (0, Maria)
    print(indice)

# lista = ['Maria','Helena', 'Luiz']
# lista.append("Lucio")
 
# for indice, valor in enumerate(lista):  # separando indice e nome em variáveis diferentes (exclusivo python)
#     print(f'Indice: {indice}', f'Valor: {valor}') # exibindo na tela formatado e bunitin indice e valor
