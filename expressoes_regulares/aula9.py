import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# Positive lookahead (?=qlqrcoisa) (verifica se o último parenteses(active-inactive) É 'active')
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

# Negative lookahead (?!qlqrcoisa) (verifica se o último parenteses(active-inactive) NÃO é 'active')
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# Positive lookahead
# pegando tudo que estiver na linha que contenha active, [negando o ^in em inactive]
# .+ para retornar as linhas que passaram na condição do lookahead
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive lookbehind(?<=) vai olhar para sua condição anterior e ver se existe atrás(behind)
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Negative lookbehind (?<!) para negação 
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

