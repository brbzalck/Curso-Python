# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

# isinstance serve para verificar qual tipo de dado é

for item in lista:
    if isinstance(item, set): # verificando se os items da minha lista é set
        print('SET')
        item.add(5) # se for vai exibir set, adicionar 5
        print(item) # exibindo novo set

    elif isinstance(item, str): # caso seja str
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)): # caso seja int ou float(basta separar por virgula os tipos de dados)
        print('NUM')
        print(item, item * 2) # para os números da lista multiplicando por 2
    else:
        print('OUTRO') 
        print(item)