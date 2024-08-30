"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


# def Print():
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# Print()

# def imprimir(): # ESCOPO BÁSICO DE UMA FUNÇÃO
#     print('olá')
# imprimir()


def saudacao(nome='Sem nome'): # def == define função, utilizado para fazer uma determinada ação ao longo do código.
    print(f'Olá, {nome}!') # Oque a função irá fazer

saudacao('Luiz Otávio') # Chamando a função definida(com o parâmetro em parenteses)
saudacao('Maria') # Parâmetros(argumentos) > São definidos para usar dentro de determinada função
saudacao() # caso tenha a possibilidade de retornar um parâmetro vazio, precisa definir um parâmetro para a própria função('Sem nome')