"""
Higher Order Functions
Funções de primeira classe
**Funções que podem receber e/ou retornar outras funções**
"""


def saudacao(msg, nome): # definindo uma função com 2 parâmetros de entrada
    return f'{msg}, {nome}!' # a função retorna os 2 parâmetros de entrada

# exemplo de função que executa função
def executa(funcao, *args): # primeiro parâmetro para função e o resto para os argumentos empacotados
    return funcao(*args) # retorna o execução da função(e os argumetos desempacotados)


print(
    executa(saudacao, 'Bom dia', 'Luiz') # executando a função que executa a função
) #                                      com os argumentos.
print(
    executa(saudacao, 'Boa noite', 'Maria')
)