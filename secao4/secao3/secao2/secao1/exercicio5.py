"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

try: # try para TENTAR executar o código, se caso for possível ou não tranformar para Inteiro o input
    num_int = int(num) # tranformando o input para Inteiro, caso não for possível vai para except e fim do programa.
    div = num_int % 2 # descobrindo se é par ou impar, pois se o resto da divisão por '2' for igual a zero = par, caso contrário impar.

    if div == 0: # SE(if) resto da div for = 0, temos par
        print(f'O número {num} é par.')
    else: # Caso contrário é impar msm.
        print(f'O número {num} é impar.')
except: # Caso não for possível tranformar para inteiro se encerra o programa e avisa o usuário.
    print('Você não digitou um número inteiro')