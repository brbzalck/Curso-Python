# import secao1
# print(secao1.dobra(2))

# Agora minha pasta secao1, se comporta como módulo(onde o __init__ da secao1, disponibiliza as importações do mesmo)

from secao1 import nova_variavel, soma_do_modulo, numero_1 # importando os modulos do __init__ da seção1

print(nova_variavel)
print(soma_do_modulo(1, 2))
print(numero_1)


