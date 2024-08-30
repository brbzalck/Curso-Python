# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None): # none nos valores de abc, caso não seja passado os parametros da fabrica_de_decoradores
    def fabrica_de_funcoes(func): # A função decoradora transforma a função original, numa closure(aguardando argumentos)
        print('Decoradora 1')

        def aninhada(*args, **kwargs): # desempacota os argumentos recebidos(lista ou dict)
            print('Parâmetros do decorador, ', a, b, c) # Posso manipulas os parâmetros da função decoradora aqui dentro
            print('Aninhada')
            res = func(*args, **kwargs) # Empacota novamente e executa função original(soma)(multiplica)
            return res
        return aninhada # sem () para criar uma closure
    return fabrica_de_funcoes # mais uma closure


@fabrica_de_decoradores(1, 2, 3) # passando uma decoradora com parâmetros, que podem ser usadas dentro do escopo da aninhada
def soma(x, y): # função simples, mas executada por meio de um decorador @fabrica_de_decoradores
    return x + y 


decoradora = fabrica_de_decoradores() #jogando a execução da fabrica_de_decoradores
multiplica = decoradora(lambda x, y: x * y) # executando minha Decoradora, e criando uma função simples em forma de lambda
subtrai = decoradora(lambda x, y: x - y) # lambda x, y == define uma função que recebe X e Y: e X - Y

dez_menos_cinco = subtrai(10, 5)
dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_menos_cinco)
print(dez_mais_cinco)
print(dez_vezes_cinco)