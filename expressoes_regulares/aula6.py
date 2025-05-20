# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação

import re

cpf = '145.654.234-86'

# ^ no começo da expressão diz que começa com, $ no final diz que termina com
# o input COMEÇA com os números diretos, e TERMINA com os numeros finalizando(vai ser um input de cpf solo)
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
# [^a-z]+ siginifica que pode ser qualquer coisa em qlqr qntd desde que NÃO contenha a-zA-Z0-9.-
print(re.findall(r'[^a-zA-Z0-9.-]+', cpf))
