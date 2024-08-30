"""
Listas em Python
Tipo list - Mutável, consegue alterar ao decorrer do cod
Suporta vários valores de qualquer tipo, varios tipos na mesma lista
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
# A LISTA É UM TIPO DE VALOR = list

#        +01234
#        -54321
# string = 'ABCDE'  # 5 caracteres (len)
# lista = [] # se estiver vazia = False
# print(bool([]))  # falsy
# print(lista, type(lista)) 

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []] # Criando uma lista
lista[-3] = 'Maria' # Trocando o valor do item na lista, endereçado em -3 (ou 2)
print(lista)
print(lista[2], type(lista[2])) # Exibindo na tela que foi trocado