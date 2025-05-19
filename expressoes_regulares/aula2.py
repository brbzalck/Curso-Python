# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )

# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# podemos utilizar | para achar x O|U y, ... diz que pode ter qualquer coisa nesse meio
print(re.findall(r'João|Maria|ad....s', texto))
print(re.findall(r'João|joão|Maria', texto))
# [Para findar tanto [J,M] quanto [j,m] em apenas uma letra de uma string]
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
# findando em range de a-z com resto de aria
print(re.findall(r'[a-z]aria', texto))
# find em range de a-z minúsculo, A-Z MAIÚSCULO e 0-9 numérico
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', texto))
# ignorando case MAIÚSCULO ou minúsculo da pesquisa
print(re.findall(r'JoÃo|MaRiA', texto, flags=re.IGNORECASE))