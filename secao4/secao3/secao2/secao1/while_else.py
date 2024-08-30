""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break # o break deixa inválido a função else em while, uma vez que break = True

    print(letra)
    i += 1
else: # Funciona com while também, mas não é muito comun
    print('Não encontrei um espaço na string.')
print('Fora do while.')