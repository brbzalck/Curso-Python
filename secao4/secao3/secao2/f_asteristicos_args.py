"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# * para empacotar e desempacotar

# def soma(x, y):
#     return x + y

def soma(*args): # *args para empacotar os argumentos dentro de uma tupla(para não precisar nomear os parâmetros)
    total = 0 # Indíce acumulativo
    for numero in args: # para cada numero dentro dos meus argumentos passado
        total += numero # soma do indice inicial == 0, com os numeros dos argumentos um a um.
    return total # retorna o total.


soma_1_2_3 = soma(1, 2, 3) # jogando na variável soma123 = a função soma(e os argumentos)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6) # jogando na variável soma456 = a função soma(e os argumentos)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros) # *var > desempacotar os itens da VAR type Tuple, tranformando em Int separados
print(outra_soma) # executando a função nos itens desempacotados e exibindo na tela

print(sum(numeros)) # sum(função) feita para somar números, dentro de um Iterável(lista, tupla)
# print(*numeros)
