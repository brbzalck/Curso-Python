# nome = input('Qual é o seu nome? ')
# print(f'Seu nome é {nome}.')
# INPUT serve para receber dados do Usuário

# numero_1 = int(input('Digite um número: '))   >>> É um jeito de resolver o problema mas não recomendado
# numero_2 = int(input('Digite outro número: '))   >>> Se o usuário digitar str o programa quebra e não vai dar p saber oque foi digitado
# resultado = numero_1 + numero_2
# print(resultado)

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1) # se o usuário digitar str ainda quebra
int_numero_2 = int(numero_2) # mas é possível saber oque o usuário digitou

resultado = int_numero_1 + int_numero_2
print(resultado)