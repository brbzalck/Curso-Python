# Empacotamento e desempacotamento de dicionários
a, b = 1, 2 # empacotado em a, b
a, b = b, a #
# print(a, b) # trocando de valor a com b


# (a1, a2), (b1, b2) = pessoa.items() # desempacotando em variáveis items do dict
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items(): # desempacotando items do dict em chave e valor
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa} # empacotando dois dict num só com **
# print(pessoas_completa)

# args e kwargs 
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs): # kwarg empacota argumentos nomeados
    print('NÃO NOMEADOS:', args) # neste caso ficam separados args - kwargs

    for chave, valor in kwargs.items(): # desempacotando em chave e valor items do kwards
        print(chave, valor) 


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes) # Desempacotando os items de um dict

# em suma kwargs desempacota dict