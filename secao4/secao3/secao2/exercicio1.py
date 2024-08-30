'''
EXERCÍCIO 1 DEFININDO UMA FUNÇÃO QUE MULTIPLICA OS ARGUMENTOS
'''
# def multiplicacao(*args): # definindo função e desempacotando os argumentos 
#     total = 1 # começando o total com 1(pois um numero multi por 1 == ele mesmo)
#     for num in args: # para cada num dos argumentos
#         total *= num # total começando com 1 e multi até o final dos argumentos
#     return total # retornadno o valor total depois do for rodar por completo
    
# resultado = multiplicacao(1, 2, 3, 4, 5)
# print(resultado)
'''
EXERCÍCIO 2 DEFININDO UMA FNÇÃO QUE DIZ SE É PAR OU IMPAR
'''

def parimpar(numero): # definindo função com parâmetro simples
    if numero % 2 == 0: # condição para se for par
        return f'{numero} é par' # caso seja retorna o primeiro return
    return f'{numero} é impar' # caso não seja retorna o segundo/próximo

print(parimpar(3)) # passando um numero INT para minha função retornar impar ou par
print(parimpar(8))
print(parimpar(17))
print(parimpar(12))