# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem"!
'''

# + significa que pode ter 1 'o' ou vários
print(re.findall(r'jo+ão+', texto, flags=re.IGNORECASE))
# * significado que pode ter nenhum 'o' ou vários
print(re.findall(r'jo*ão*', texto, flags=re.I))
# ! significa que 'o' pode existir OU não(apenas 1 ou 0)
print(re.findall(r'jo?ão?', texto, flags=re.I))
# {1,} significa que pode haver 1 'o' OU ilimitadas vezes
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
# {min, max} e só pode ter no máximo 3, e m 1 ou 2
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
# + significa que pode ter 1 ou vários caracteres de a-z desde que estaja entre j---ão
print(re.findall(r'j[a-z]+ão+', texto, flags=re.IGNORECASE))

texto2 = 'João ama ser amado'
# verifica se tem ama + [uma das duas letras 'do'],{duas vezes para achar d+o = amado}
print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I))