"""
Tipo tupla - Uma lista imutável
"""
# *** DESENPACOTANDO ITEM DA LISTA ***

# atribui variáveis separadas por virgulas (_), até chegar no item desejado colocando a variável especifica(nome)
# _, nome, *_ = ['andre', 'lucas', 'joao', 'julia', 'marcela', 'ingrid'] # *_ == para todo o resto
# print(nome) # Pegando o segundo valor

# Tipo tupla - Uma lista imutável 
# A única diferença é que a tupla é com () e lista com []
# lista pode mudar os valores, tuple não pois é imutável

nomes = ('Maria', 'Helena', 'Luiz')
# nomes = list(nomes) # transformando uma tuple em lista
# nomes = tuple(nomes) # transformando uma lista em tuple
print(nomes)