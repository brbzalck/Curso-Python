# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

print(*produtos, sep='\n')
print('normal')
'''_______________________________________________________________________________________________________________________'''

produtos_com_desconto = copy.deepcopy(produtos) # Fazendo uma deepcopy(para poder editar diferentes lista de uma mesma) 
novos_produtos = [{**produto, 'preco': round(produto['preco'] * 1.1, 2)} for produto in produtos_com_desconto]
# listC [{desempacotando o dict, definindo preço + round na expressão(formata float para 2casas)}]
print(*novos_produtos, sep='\n') # sep='\n' quebra linha
print('preço 10% a mais')
'''_______________________________________________________________________________________________________________________'''
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos) # Fazendo um deepcopy dos preços ajustados
produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda item: item['nome'], reverse=True) #reverte a ordem
# nova lista = sorted(oragniza)(nova lista, cria uma funçao sem nome| item: item[''] define por onde organizar)
print(*produtos_ordenados_por_nome, sep='\n') #sep='\n' quebra linha
print('nome ordem decrescente')
'''_______________________________________________________________________________________________________________________'''
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key=lambda item: item['preco'])
# lista preço = sorted(organiza)(lista preço, função sem nome item: item['Define o parâmetro'])
print(*produtos_ordenados_por_preco, sep='\n') # sep='\n' quebra linha
print('por preço crescente')
