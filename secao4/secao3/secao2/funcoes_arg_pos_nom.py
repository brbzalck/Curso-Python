"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z): # Definindo função e seus parâmetros
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)
    # x= faz aparecer o parâmetro junto com o argumento(mesma coisa que x={x})


soma(1, 2, 3) # Executando a função com os argumentos selecionados para o parametro da função
soma(1, y=2, z=5) # x == 1, y == 2, z == 5, exemplo de arugumento nomeado
# É o caso usar somento argumento não nomeado, ou então, apenas nomeado(caso precise alterar a ordem)
print(1, 2, 3, sep='-') # x= tem a mesma função que sep='-', que fica x-1 x=1