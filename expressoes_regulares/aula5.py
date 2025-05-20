# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3

import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

# *? -> faz o find pegar o primeiro match e já deixar separado non-greedy (lazy) -> comportamento não guloso
# chamando pela variável \2 que armazena qual () se trata -> basta contar com (1(2(3
# como estamos usando () primeiro a regex retorna o find do primeiro (), depois do segundo ()
# para cada parenteses temos um retorno da regex
tags = re.findall(r'(<([pdiv]{1,3})>(.*?)<\/\2>)', texto)
pprint(tags)

for tag in tags:
    um, dois, tres = tag
    print(tres)

print()

cpf = '145.654.234-86'
# Procurando no texto uma sequência que siga o padrão completo de CPF:
# procurando no cpf uma combinação do cpf inteiro contida no primeiro parenteses
# segundo parenteses, vai para pegar os três primeiros números com o ponto: 123.
# ?: para não retornar ele apenas guardar o valor
# {2} ao lado direito de () para repetir 2 vezes essa expressão
# 3 numeros de 0-9 com '-' no final, finalizando com 2 números de 0-9
# procurar tudo isso em cpf 
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# substituindo no texto onde temos tag, texto, tag
# o primeiro parenteses captura a primeira tag
# dentro do primeiro parenteses o segundo armazena o nome da tag(pode ser qlqr coisa .+ não guloso ?)
# o terceiro parenteses pega o conteudo que fica entre as tags (pode ser qlqr coisa .+ não guloso ?)
# o quarto parenteses repete o segundo, que é o conteúdo da tag <p> ou <div> para casar a tag com fechamento
# retorno da expressão com r'\1 variável que contem o primeiro parenteses, e assim vai, concatenando substituição'
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))