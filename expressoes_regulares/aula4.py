# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''
# <[pode ser p ou div]{contendo 1(p) até 3(div)}>
# .* significa que pode haver nada ou N coisas dentro das tags p, div
# usando a \ para clenar / -> boa pratica
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))
# mesma coisa de cima, só que com .*? -> faz o find pegar o primeiro match e já deixar separado
# non-greedy (lazy) -> comportamento não guloso
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))