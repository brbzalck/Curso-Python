# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda', # dict
}

pessoa.setdefault('idade') # método para caso não haja determinada chava, == None ou Xvalor
# print(len(pessoa)) # método para descobrir quantas chaves eu tenho
# print(list(pessoa.keys())) # método keys para retornar as chaves do dict
# print(list(pessoa.values())) # método values para retornar os valores de dict
print(list(pessoa.items())) # método itens para retornar as chaves e valores do dict
print('')
# for valor in pessoa.values(): # para cada valor dos valores das pessoas
#     print(valor)

for chave, valor in pessoa.items(): # para cada chave e valor do dict pessoa.items > metodo
    print(chave, valor) #exiba chave e valor