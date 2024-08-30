"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

# É mais uma maneira de formatar a str, com %(tipo de dado) ex %d que seria um dado tipo int
# Em seguida basta colocar entre parentes as variáveis do lado da str a ser preenchida
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))