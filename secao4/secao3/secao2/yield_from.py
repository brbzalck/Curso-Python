# Yield from
def gen1(): # 
    print('COMECOU GEN1')
    yield 1 # pausa a função no meio da execução e retorna 1(linha 31)
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20 # em suma, yield serve para parar a função e fazer outra coisa(doidera)
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen # pausando a função e executando a função determinada pelas VAR(g1,g2,g3)
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1: # Iterando uma função
    print(numero) # retornando os valores de yield
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()