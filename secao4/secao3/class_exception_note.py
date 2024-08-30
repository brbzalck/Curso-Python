# Criando Exceptions em Python Orientado a Objetos

# Notas das exceptions em Python (add_notes, __notes__)

# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Levantando e tratando suas Exceptions (Exceções)
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

# AULA VOLTADA PARA QUANDO FOR ESPECIFICAR ERRO ESPECÍFICO DO MEU CODIGO

class MeuError(Exception): # Meu erro especifico que herda de Exception
    ...


class OutroError(Exception): # Meu outro erro específico que herda de Exception
    ...


def levantar(): 
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Esse é o erro')
    raise exception_ # Executa MeuError(Com as msg especificas de erro)


try:
    levantar() # Gerando MeuErro
except (MeuError, ZeroDivisionError) as error: # Tratano meu erro especifico numero 1
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo') # Tratano meu erro especifico numero 2
    exception_.__notes__ = error.__notes__.copy() # Fazendo uma junção dos erros
    exception_.add_note('Toma mais um so p ficar esperto')
    raise exception_ from error # lançando uma exeção dentro de outra exeção