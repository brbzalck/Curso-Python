""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operadores = input('Escolha um operador: (+) (-) (/) (*). ')

    flag = None # Criando uma bandeira com valor NONE

    num1 = 0 # Criando VAR fora do bloco para nao dar problema
    num2 = 0 # Criando VAR fora do bloco para nao dar problema
    
    try: # Tentar executar ( Em caso de o usuário não mandar Numeros p calcular)
        num1 = float(numero_1) # Agora sim atribuo valor
        num2 = float(numero_2) # Agora sim atribuo valor
        flag = True # Tanformando a Flag em True para pular linha 19
    except: # Caso contrário...
        ...
    if flag is None: # Caso o try dê erro e o flag não trocar seu valor, exibe mensagem de erro ao usuário.
        print('Você digitou um ou ambos números errado. ')

    operadores_permitidos = '+-/*' # Definindo os operadores previstos

    if operadores not in operadores_permitidos: # Se o operador digitado não existir dentro da VAR operadores_permitidos, exibe mensagem de erro
        print('Digite corretamente o Operador.')
    
    if len(operadores) > 1: # len para ver se não foi digitado mais de um Operador
        print('Por favor, apenas 1 operador.')

    print('Realizando sua conta, confira abaixo:')

    if operadores == '+': # se o operador for + 
        print(f'{num1} + {num2} = ', num1 + num2) # String mostrando os Numeros digitados + soma
    elif operadores == '-': # se o operador for -
        print(f'{num1} - {num2} = ', num1 - num2) # String mostrando os Numeros digitados + subtração
    elif operadores == '/': # se o operador for /
        print(f'{num1} / {num2} = ', num1 / num2) # String mostrando os Numeros digitados + divisão    
    elif operadores == '*': # se o operador for * 
        print(f'{num1} * {num2} = ', num1 * num2) # String mostrando os Numeros digitados + multiplicação
    else:
        print('Deu bleybleyd')

    #             Converte td pra minpusculo e depois verifica se começa com 's'
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    # VAR que incialmente era str, o primeiro método retorna str, e por fim o ultimo método 
    #                                                                                  Bool
    if sair is True:
        break