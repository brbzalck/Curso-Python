# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero') # Exibindo minha própria mensagem de erro
    return True 


def deve_ser_int_ou_float(n): # função que verifica int ou float
    tipo_n = type(n) # pegando o tipo de dado de n(ou d)
    if not isinstance(n, (float, int)): # se nao for instancia de int ou float
        #raise para trocar a mensagem do erro, pelo oque eu quiser
        raise TypeError( 
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        ) # ****lançando minha própria msg de erro****
    return True


def divide(n, d): # função que recebe dois argumentos
    deve_ser_int_ou_float(n) # verifica com a função linha9 n
    deve_ser_int_ou_float(d) # verifica com a função linha9 d
    nao_aceito_zero(d) # verifica se d == 0
    return n / d # por fim, todos os erros ja tratados, divide os argumentos


print(divide(8, '0'))

raise TypeError()
raise IndexError()