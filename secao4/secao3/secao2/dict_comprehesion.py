# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul', # dict
    'preco': 2.5, 
    'categoria': 'Escritório',
}


# exemplo de dict comprehesion
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}
#                                   ternária de verificação se o valor do dict é str, caso contrário retorne só o valor sem upper
dc1 = {chave.upper(): valor.upper() if isinstance(valor, str) else valor for chave, valor in produto.items() if chave != 'preco'}
#Exemplo de dict comprehesion, com dois valores retirados do dict pelo .items, com o método upper            filtro utilizado para tirar a chave preco


print(dc1)



lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista # tranformando uma lista de tupla em dict, é necessário que se pareça com um dict para isso
}

print(dc)

s1 = [2 ** i for i in range(10)] 
print(s1)