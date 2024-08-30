# reduce - faz a redução de um iterável em um valor


from functools import reduce # IMPORTANDO REDUCE

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


# def funcao_do_reduce(acumulador, produto): # Função que recebe 2 parâmetros
#     return acumulador + produto['preco'] # soma o acumulador = 0 (linha22), com preço do produto


# Reduce é utilizado para fazer a redução de dados a um. Ex Somatória de 5 numeros p 1
total = reduce(lambda x, y: x + y['preco'], produtos, 0)
print('Total é', total)


# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

print(sum(p['preco'] for p in produtos))