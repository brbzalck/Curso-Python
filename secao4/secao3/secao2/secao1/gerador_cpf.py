import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    mult = 10 
    resultado = 0 

    for num in nove_digitos: # Para cada num nos nove digitos
            cpf_int = int(num) # Tranformando para inteiro minha str
            conta = cpf_int * mult # conta do cpf * 10
            resultado += conta # contacetenando o resultado da conta na minnha VAR vazia
            mult -= 1 # Diminuindo 1 da VAR mult conforme pedido pelo eneciado do problema

    conta_final = (resultado * 10) % 11 # conta final vai ser o resultado depois de passar pelo for * 10, depois calcular o resto da divisão por 11

    primeiro_num = conta_final if conta_final <= 9 else 0 # O primeiro número calculado
    # O número calculado só vai ser o número calculado se for menor ou igual a 9, caso contrário vai ser 0

    ### JEITO DO PROFESSOR ###

    dez_digitos = nove_digitos + str(primeiro_num) # agora com 10 digitos, vou somar os noves digitos(str) com o primeiro número calculado(int)
    #                                                                                        fazendo a coerção para str, fazendo possível concatenar
    mult2 = 11
    resultado_2 = 0

    for num2 in dez_digitos: # para cada num nos 10 digitos
            resultado_2 += int(num2) * mult2 # concatenando o resultado da conta(começa com 0), com meu 1°num dos 10num ja tranformado para int * 11
            mult2 -= 1 # Tirando um do multiplicador para fazer jus ao enunciado

    conta_final2 = (resultado_2 * 10) % 11 # multiplicando o resultado da iteração dos 10num multiplicados em ordem decrescente, e dividindo pelo resto
    #                                                                                                                          da divisão por 11
    segundo_num2 = conta_final2 if conta_final2 <= 9 else 0 # O segundo numero calculado
    # O segundo numero calculado só vai ser o segundo número calculado se for menor ou igual a 9, caso contrário será 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_num}{segundo_num2}'

    print(cpf_gerado_pelo_calculo)