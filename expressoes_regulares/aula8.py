# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $ -> Find no começo e fim de cada linha
# re.S -> Dotall \n -> faz o find reconhecer quebrar de linha também

import re

texto = '''
131.768.460-53 ABC
055.123.060-50 def
955.123.060-90
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', texto, flags=re.M))

texto2 = '''O João gosta de folia 
E adora ser amado'''

# começa com o, qlqr merda no meio, termina com o. flag re.I para Case e re.S para reconhecer \n
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
