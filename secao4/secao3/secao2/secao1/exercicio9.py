"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os # importando uma biblioteca

palavra_secreta = 'python' # Definindo a palavra secreta
letras_acertadas = '' # str vazia para armazenar a iteração da sobre str
qnt_chutes = 0

while True: # Como não sei quantas vezes o Código vai rodar = WHILE
    letra_digitada = input('Digite uma letra: ') # Chute do usuário
    qnt_chutes += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra por vez.')
        continue

    if letra_digitada in palavra_secreta: # verificando se a letra digitada esta na palavra secreta
        letras_acertadas += letra_digitada # Atribuindo a str vazia criada no inicio do programa, a letra digitada que faz parte da palavra secreta.

    palavra_formada = '' # criando uma str vazia para armazenar a iteração da str(palavra_secreta)
    for letra_secreta in palavra_secreta: # Iterando a palavra_secreta ( p y t h o n ) na variável letra_secreta
        if letra_secreta in letras_acertadas: # se alguma letra da Iteração (p y t h o n), estiver entre as letras_acertadas e definidas pela linha31
            palavra_formada += letra_secreta # caso a letra_acertada esteja certa, concateno a letra_secreta na palavra_formada
        else:
            palavra_formada += '*' # caso a letra não estaja certa, coloque * na concatenação de palavra_formada
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta: 
        os.system('cls') # faz o terminal code limpar antes de exibir os prints abaixo
        print('VOCÊ GANHOU, PARABENS!!!')
        print('A palavra era:', palavra_secreta)
        print(f'Tentativas:', qnt_chutes)
        break # termina a repetição


        

