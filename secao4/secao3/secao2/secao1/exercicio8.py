'''
Iterando strings com while

#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*L*u*i*z* *O*t*á*v*i*o'
'''

nome = input('Digite seu nome: ')

indice = 0 # Indicando o início p contar até chegar no Len(qnt de letras da str)
novo_nome = '' # Criando uma str vazia, para colocar as letras de uma a uma

while indice < len(nome): # Exectuta se o Len for maior que o indice
    letra = nome[indice] # pegando letra por letra, variando o indice e iterando a str
    novo_nome += f'*{letra}' # Concatenando letra com letra e asteristico
    indice += 1 # subindo o indice até chegar no Len
novo_nome += '*' # Colocando o ultimo asteristico
print(novo_nome)
