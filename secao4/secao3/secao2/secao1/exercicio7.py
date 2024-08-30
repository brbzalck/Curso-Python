"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual é o seu primeiro nome? ')
qtd_nome = len(nome)

if qtd_nome <= 4:
    print('Seu nome é curto')
elif qtd_nome == 5 or qtd_nome == 6:
    print('Seu nome é normal')
elif qtd_nome > 6:
    print('Seu nome é muito grande')
else:
    print('Tente novamente.')