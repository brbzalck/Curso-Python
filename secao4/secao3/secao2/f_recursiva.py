# FUNÇÃO RECURSIVA TEM O MESMO OBJETIVO DO LOOP, RETORNANDO ELA MESMA


def recursiva(inicio=0, fim=4):


# import sys
    print(inicio, fim)
# sys.setrecursionlimit(1004)

    # Caso base
    if inicio >= fim:
        return fim # TERMINANDO A FUNÇÃO CASO O INICIO CHEGUE NO FIM

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1 # ADICIONANDO MAIS UM NO INICIO
    return recursiva(inicio, fim) # RETORNANDO A PRÓPRIA FUNÇÃO(LOOP) SIMILAR AO FOR/WHILE
# def recursiva(inicio=0, fim=4):

#     print(inicio, fim)

print(recursiva())
#     # Caso base
#     if inicio >= fim:
#         return fim

#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva(0, 1001))

def factorial(n):
    if n <= 1: # SE O N FOR MENOR OU IGUAL A 1
        return 1 # ENCERRA E RETORNA

    return n * factorial(n - 1) # RETORA A PRÓPRIA FUNÇÃO, DIMINUINDO 1 DO ARGUMENTO


print(factorial(5))
print(factorial(10))
print(factorial(100))



fatorial = 100

for x in range(fatorial):
    y = x * fatorial
    fatorial - 1

print(y)