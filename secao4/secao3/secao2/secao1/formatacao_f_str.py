"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # Coloca 10 cazas antes da variável
print(f'{variavel: <10}.') # dps
print(f'{variavel: ^10}.') # no meio
print(f'O hexadecimal de 1500 é {1500:08X}') # :08X da esq p dir : chama a função 0 preenche
print(f'{variavel!r}') #                  8 oito vezes X tranforma em hexadecimal