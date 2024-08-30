"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao): # criando função com um parâmetro
    def saudar(nome): # criando uma subfunção com outro parâmetro
        return f'{saudacao}, {nome}!' # a subfunção, retorna saudação e nome
    return saudar # tirando os parênteses para não executar saudar
# e apenas guardar os dados da função por enquanto
# UTILIZADO PARA CONSEGUIR PASSAR OS ARGUMENTOS DE SAUDAR (NOMES) SOMENTE DEPOIS (LINHA17)


falar_bom_dia = criar_saudacao('Bom dia') # variável executando função criar_saudacao
falar_boa_noite = criar_saudacao('Boa noite') # e argumento de boa noite ou bom dia


for nome in ['Maria', 'Joana', 'Luiz']: # para cada nome da lista
    print(falar_bom_dia(nome)) # executando função guardada na var falar_bom_dia
    print(falar_boa_noite(nome)) # com argumento(nome) para cada item da lista