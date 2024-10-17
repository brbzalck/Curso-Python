# sys.argv - Executando arquivos com argumentos no sistema
'''Serve para ver se o módulo foi executado com argumentos'''

import sys

argumentos = sys.argv  # Pegando quais argumentos existem na execução do sistema python # noqa 501
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')
