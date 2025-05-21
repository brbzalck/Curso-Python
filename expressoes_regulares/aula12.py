import re

# https://regex101.com/r/DfXYXM/1/

# ^ garantindo que começe a verificação pelo começo da string

# ?: usado para não capturar como retorno essa condifcional (apenas o match final)
# \(, \) para colocar parenteses() literal na pesquisa
# \d{2} verifica se existe 2 números dentro dos parenteses literal
# \s significa que nesse campo existe um espaço literal
# juntando tudo até aqui temos um verificação de "(24)""

# ?: não captura o valor da condicional (apenas o match final)
# 9 literal
# \s espaço em branco literal
# juntando tudo até aqui temos "9 "

# ?: não captura o valor da condicional (apenas o match final)
# \d{4} diz que deve haver 4 números aqui
# - literal
# \d{4} diz que existe mais 4 números aqui
# juntando tudo nessa condicional temos "0000-0000"

# $ garantindo que termine ao fim da linha

regexp = re.compile(r'^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4})$', flags=re.M)

texto = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''

for telefone in regexp.findall(texto):
    print(telefone)