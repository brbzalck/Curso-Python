# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # nonlocal é usado quando for preciso, acessar uma VAR fora do escopo da função
        valor_final += valor_a_concatenar # depois do nonlocal conseguir o valor da VAR do escopo de cima > concatena
        return valor_final
    return interna # subfunção sem (), para guardar os dados da função primária e passar o argumento da interna futuramente


c = concatenar('a') # passando o argumento da função primária 
print(c('b')) # agora, com a função pausada, o argumento da subfunção é passado
print(c('c'))
print(c('d'))
final = c()
print(final)