# try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e: # Usando o except para tratar possíveis erros
    print(e.__class__.__name__)
    print(e)
except NameError: # pode ser usado mais de 01 except
    print('Nome b não está definido')
except (TypeError, IndexError) as error: # e também pode ser usado 02 erros no mesmo except
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception: # exception, má prática de programação, usado para não quebrar o código de jeito nenhum
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')