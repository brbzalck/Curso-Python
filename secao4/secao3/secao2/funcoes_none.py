"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""


def soma(x, y, z=None): # Utilizando None como valor padrão, caso o valor possa ser passado ou não
    if z is not None: # Caso o valor tenha sido passado
        print(f'{x=} {y=} {z=}', x + y + z) # Mostrando na tela com o valor Z inserido
    else: 
        print(f'{x=} {y=}', x + y) # print sem o Z


soma(1, 2) # x y
soma(3, 5) # x y
soma(100, 200) # x y
soma(7, 9, 0) # x y z
soma(y=9, z=0, x=7) # x y z