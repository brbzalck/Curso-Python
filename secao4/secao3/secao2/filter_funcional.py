# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n') # Função para formatar desempacotando a lista e por quebra de linha meu dict
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# def filtrar_preco(produto): # função que retorna os preços maiores que 100
#     return produto['preco'] > 100 


# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]
novos_produtos = filter(lambda x: x['preco'] > 100, produtos)


print_iter(produtos)
print_iter(novos_produtos)