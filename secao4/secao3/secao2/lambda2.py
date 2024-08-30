def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)
duplica = executa( # lambda precisa estar em um função que executa ela (linha1)
    lambda m: lambda n: n * m, # lambda representada em função que retorna função
    # def função = lambda , () = m: | def subfunção = lambda , () = n:
    3 # passando o valor de m
)
print(duplica(2)) # chamando a função guardada na VAR duplica com o valor para (n)

print(
    executa( # chamando a função executa para executar minha lambda
        lambda x, y: x + y, # lambda = def soma , x, y: = (x, y): | x + y
        2, 3 # passando os argumetos dentro da propria função
        # mas poderia passar por meio de uma VAR fora da função
    ),
)

print(executa(
        lambda *args: sum(args), # lamda = def somatoria , *args: = (*args): sum(args)
        1, 2, 3, 4, 5, 6, 7 # passando os argumentos dentro na propria função lambda
    ))
