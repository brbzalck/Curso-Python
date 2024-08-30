"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    if x > 10:
        return [10, 20] # return é usado quando quiser que a função retorne algum valor(salvando na memória) 
    return x + y # assim que a função retornar algo, oque estiver para baixo da mesma não executará


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1) # return linha 9
print(soma2) # return linha 9
print(soma(11, 55)) # return linha 8 - 11 é maior que 10