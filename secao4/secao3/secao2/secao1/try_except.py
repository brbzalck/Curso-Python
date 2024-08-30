"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try: # Tenta executar até onde der, Caso der errado vai para except
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except: # Ao dar errado no try, continua daqui.
    print('Isso não é um número')

# if numero_str.isdigit(): # verifica se o usuário digitou somente Numero retornando em Booleano
#    numero_float = float(numero_str) # Tranformando para str do input float
#    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') # Multiplicando o Float por 2 com 2 casas Decimais > :.2f
# else:
#    print('Isso não é um número')