# Ordem dos decoradores
def parametros_decorador(nome): # parametro do meu decorador recebe nome
    def decorador(func): # decoradora que recebe função
        print('Decorador:', nome) # manipulando nome dentro do escopo da minha decoradora

        def sua_nova_funcao(*args, **kwargs): # desempacotando os argumentos, e obtendo uma nova função a partir da função original
            res = func(*args, **kwargs) # Executando a função e empacotando novamente o resultado
            final = f'{res} {nome}' # Colocando os resultados dos parâmetros de soma e nome na mesma f'{var}str'
            return final
        return sua_nova_funcao # closure
    return decorador # closure


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2') # com ordem de baixo para cima
@parametros_decorador(nome='1') # decorador com mais de um parâmetro empilhado
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)