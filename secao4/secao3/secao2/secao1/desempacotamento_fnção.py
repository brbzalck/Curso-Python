# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
# lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# p, b, *_, ap, u = lista # Atribuindo a VAR valor especifico, e colocando o resto em uma VAR que não vai usar == *_
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista) # exibe na tela de forma desempacotada, chamo uma função e desempacoto com * antes da VAR
# print(*string) # Funciona com string e itera a mesma
# print(*tupla) # Funciona com tupla, exibindo fora dos ''

# print(*salas, sep='\n') # *salas = Desempacota a minha lista, sep='\n' = quebra minha linha nos espaços vazios

lista = ['Maria', 'Lucas', 'José']
dicio = {'nome: lucas', 'peso: 70'} 

def desempacota(args):
    print(*args)

desempacota(lista)