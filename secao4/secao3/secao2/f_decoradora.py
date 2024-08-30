# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func): 
    def interna(*args, **kwargs): # desempacota o argumento para verificação
        print('Vou te decorar')
        for arg in args: # para cada arguemento(letra) dos meus argumentos(str) 
            e_string(arg) # chamando a função e_string para verificar se o arg é str
        resultado = func(*args, **kwargs) # invertendo a str com a função recebida como argumento da função principal
        print(f'O seu resultado foi {resultado}.') # str invertida
        print('Ok, agora você foi decorada')
        return resultado # função retorna resultado
    return interna # função sem parenteses para guardar os dados e executar somente depois(linha30)


def inverte_string(string): # Função que inverte a string recebida
    return string[::-1] # começando a str pelo último índice (::-1), invertendo a str


def e_string(param): # Função que verifica se o argumento é str
    if not isinstance(param, str): # se não for instancia de str
        raise TypeError('param deve ser uma string') # exiba o erro com método raise TipoDeErro('msg qlqr')

lista = ['lucas', 'maria', 'jose']

inverte_string_checando_parametro = criar_funcao(inverte_string) # Jogando a função que recebe função numa VAR
invertida = inverte_string_checando_parametro('123') # Passando o argumento para sub função trabalhar
print(invertida)

# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao # Exemplode de decorador @nome_da_função_decoradora em cima da função desejada
def inverte_string(string): 
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123') # Agora basta chamar a função de fato com o arugumento desejado
print(invertida)