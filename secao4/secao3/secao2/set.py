# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno (muda oque tem dentro, mas não aceita oque entra ser mudado(ex listas ou dict))

'''________________________________________________________________________________________________________________________________________________'''

# Criando um set

print('CRIANDO UM SET(CONJUNTO)')
var = set('Luiz') # set(iterável)
var = set()  # vazio
var = {'Luiz', 1, 2, 1.1, 3}  # Criando set com dados, set = {x, y, z} só aceita imutável
print(var) 
print()
print()

'''________________________________________________________________________________________________________________________________________________'''

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

print('RETIRANDO VALORES REPETIDOS + FOR set')
l1 = [1, 2, 3, 3, 12, 19, 6, 3, 3, 3, 1] # Lista com valores repetidos
set1 = set(l1) # usando a Class set(l1) para remover os valores repetidos da lista
l2 = list(set1) # transformando em lista novamente
print(l2) 
print(3 not in set1) # not in
for numero in set1: # for in
    print(numero)
print()
print()

'''________________________________________________________________________________________________________________________________________________'''

# Métodos úteis:
# add, update, clear, discard

print('MÉTODOS EM SET(CONJUNTO)')
met = set() # Conjunto set vazio
met.add('Luiz') # .add para adicionar um imutável para o Conjunto
met.add(1) # Adicionando número
met.update(('Olá mundo', 2, 3, 4)) # update para adicionar vários valores(em formato de tupla=imutável&iterável)
# s1.clear() # Limpa todo Conjunto
met.discard('Olá mundo') # .discard(dado imutável em especifico) apaga o dado desejado
# s1.discard()
print(met)
print()
print()

'''________________________________________________________________________________________________________________________________________________'''

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

print('OPERADORES DE CONJUNÇÃO')
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 # | para unir
s4 = s1 & s2 # & faz parte de ambos
s5a = s1 - s2 # - Diferença de itens para esquerda
s5b = s2 - s1 # - Diferença de itens para esquerda
s6 = s1 ^ s2 # ^ resto que sobrou da intersecção

print(s3, 'uniao')
print(s4, 'interscção')
print(s5a, 'diferença de s2 em s1')
print(s6, 'sobra')