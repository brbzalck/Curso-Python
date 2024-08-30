# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def dupli(numero):
#     dupl = numero * 2
#     return f'O dobro de {numero} é {dupl}'

# def tripli(numero):
#     tripl = numero * 3
#     return f'O triplo de {numero} é {tripl}'

# def quadri(numero):
#     quadr = numero * 4
#     return f'O quadruplo de {numero} é {quadr}'

# print(dupli(2))
# print(tripli(2))
# print(quadri(2))


'''
Automatizado
'''

def criar_multiplicador(multiplicador): # criando uma função para fazer a conta
    def conta(numero): # subfunção para pegar o número
        return numero * multiplicador # multiplicando numero pelo multiplicador
    return conta # função sem parenteses, para passar meu número separadamente

duplicar = criar_multiplicador(2) # criando os multiplicadores
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(f'O dobro é:', duplicar(2)) # Usando minha VAR com a função armazenada
print(triplicar(2)) # e colocando (argumento da minha subfunção)
print(quadruplicar(2))