

entrada = input('Digite um número: ')

if entrada.isdigit(): # Conferindo se o número é um digito NUMÉRICO
    entrada_int = int(entrada) # Tranformando um número Inteiro
    par_impar = entrada_int % 2 == 0 # Conferindo se a expressão é igual a zero, Retornando um Booleano entre False ou True


    par_impar_texto = 'ímpar' # Atibuindo um valor inicial para VAR par_impar_texto no caso do If debaixo não executar (se a VAR par_impar for
#False por exemplo) ( se a expressão der =! 0, retorna False )


    if par_impar: # Caso a VAR par_impar for TRUE ( se a expressão der == 0, retorna True )
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}') # print pertencente ao primeiro If, variando a VAR pela linha 10 ou 14.
else:
    print('Você não digitou um número inteiro...')
