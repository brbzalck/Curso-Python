# # Introdução à List comprehension em Python
# # List comprehension é uma forma rápida para criar listas
# # a partir de iteráveis.
# # print(list(range(10)))

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# mesma coisa da linha4
lista = [] # lista vazia
for numero in range(10): # para cada numero de um a 10
    lista.append(numero) # adiciona a lista
# print(lista)


# List comprehension
lista = [ # usando a função para criar uma lista multiplicado por 2 de 0 a 9(range10)
    numero * 2 # [>numero +-*/< para cada numero de 0 a 9(range 10)] ex:
    for numero in range(10) # [numero * 2 for numero in range(10)] 
] #                         multiplica cada índice por 2
print(lista)

'''______________________________________________________________________________________'''

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, }, # lista de produtos armazenados no dict
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [ # atualizando a lista seguindo a regra da lógica ao lado esquerdo do for
    {**produto, 'preco': produto['preco'] * 1.05} # #desempacotar do dict, e redefinir o preço
    # com 'preço': < atribuição| produto['preço'] < pegando valor de preço| * 1.05 < calcula aumento de 5%
    for produto in produtos # para cada produto dos meus produtos(dict com nome e preço)
]

# # print(novos_produtos)
# print(*novos_produtos, sep='\n')
'''_____________________________________________________________________________________'''

# Filto list comprehension #If ao lado de for#


# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]


# apliquei 20 por cento de desconto apenas nos produtos abaixo de 10 reais
novos_produtos = [
    {**produto, 'preco': produto['preco'] - produto['preco'] * 0.20 } # << Mapeamento de dados
    for produto in produtos # para cada dict da minha lista
    if produto['preco'] <= 10 # if depois do for para adicionar fitro com IF
]
p(novos_produtos)# p=modulo pprint para exibir formatado