# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda', # dict
}

#################### GET

print(p1['nome']) 
print(p1.get('nome', 'Não existe')) # método get retorna None caso a chave não exista
#                               e não deixa quebrar o código

#################### POP

# nome = p1.pop('nome') # método pop exclui determinada chave
# print(nome) # e retorna a chave excluida
# print(p1) # mas ela deixa de fazer parte do dict

#################### POPITEM

# ultima_chave = p1.popitem() # exclui a última chave do dict
# print(ultima_chave) # retorna a última chave
# print(p1) # mas deixa de fazer parte do dict

#################### UPDATE

# p1.update({ 
#     'nome': 'novo valor', # método update utilizado para atualizar ou criar items no dict
#     'idade': 30,
# })

p1.update(nome='novo valor', idade=30) # maneira mais simples de usar o método
# tupla = (('nome', 'novo valor'), ('idade', 30)) 
lista = [['nome', 'novo valor'], ['idade', 30]] # lista dentro de lista
p1.update(lista) # atualizando uma lista dentro do dict
print(p1)

