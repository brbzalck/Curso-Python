# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


# F Closure serve para não executar a função, e guardar os dados, executando futuramente por meio de uma variável(argumento=y)

def criar_funcao(funcao, x): # criando uma função que recebe outra função e somente um parâmetro
    def interna(y): # criando uma subfunção que ADIA a execução da função primária, recebendo o valor de interna(y) futuramente
        return funcao(x, y) # ja com X recebido na função1 e Y na função2, executa a função externa
    return interna # retornando a função sem () para ADIAR a execução e receber o argumento futuramente

soma_com_cinco = criar_funcao(soma, 5) # jogando a função criar_função, com a função soma e argumentos, para uma VAR
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(15)) # chamando a VAR que guarda a função, e passando valor de Y
print(multiplica_por_dez(10))