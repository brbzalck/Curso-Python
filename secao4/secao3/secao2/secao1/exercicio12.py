"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import re # Módulo utilizado para selecionar apenas números
import sys # Módulo utilizado para encerrar o programa caso necessário


cpf = input('Digite seu cpf: ')# .replace('.', '').replace('-', '').replace(' ', '') 
# repleace é um método que pode ser utlizado caso queira substiruir caracteres por outro, .repleace('sai esse', 'entra esse')
cpf_enviado_usuario = re.sub(r'[^0-9]', '', cpf) # Utilizando a função .sub do módulo re, para selecionar apenas numeros de [0 a 9]
# == r'[^0-9]' significa selecionar tudo que não é um número(^0-9), e substituir para (''), da minha str da VAR cpf
nove_digitos = cpf_enviado_usuario[:9] # pegando os nove primeiros N° do cpf_eviado_usuario ja formatado em somente numeros pela linha 33.


entrada_sequencial = cpf == cpf[0] * len(cpf) # condicional para se meu cpf for igual ao indice 0 do cpf * qntd de caractere do meu cpf
#                                   Neste caso para se o usuário mandar números repetidos, ex: indice 0 do cpf * len do cpf == 11111111111
if entrada_sequencial: # se for True
      print('Cpf inválido') 
      sys.exit() # Utilizando o múdulo sys e método exit para encerrar o python


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


cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_num}{segundo_num2}' # juntando os nove digitos com o 1°num calculado e 2°num calculado

if cpf_gerado_pelo_calculo == cpf_enviado_usuario: # se o cpf gerado pelo calculo for igual ao cpf enviado 
    print(f'O cpf {cpf_enviado_usuario} é valido') # É válido
else:
    print('Cpf inválido') # Caso contrário inválido



"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
