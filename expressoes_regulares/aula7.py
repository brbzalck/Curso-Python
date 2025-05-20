# minúsco confirma MAIÚSCULO nega nos atalhos \w \W \d \D \s \S

# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> flag=re.A tira a validação de find dos acentos, aceitando apenas letra e numeros
# \W -> [^a-zA-Z0-9À-ú_] -> faz a negação de \w
# \W -> [^a-zA-Z0-9_] -> re.A -> faz a negação de \W com re.A(reornando apenas as letras com acentos)
# \d -> [0-9] -> atalho para retornar números
# \D -> [^0-9] -> atalho para NÃO retornar números
# \s -> [ \r\n\f\v\t] -> captura todos os espaços em branco do seu texto
# \S -> [^ \r\n\f\v\t] -> captura tudo que não for espaço(apenas palavras)
# \b -> borda -> finda oque estiver em \b(qlqr coisa)\w+(oque tiver pra cá)
# \B -> não borda

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''


# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z]+', texto))
# print(re.findall(r'[a-zA-Z0-9]+', texto))

# À-ú inclui acentos
# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# \w+ faz a mesma verificação de [a-zA-Z0-9À-ú]+
# print(re.findall(r'\w+', texto))
# print(re.findall(r'\W+', texto))
# print(re.findall(r'\d+', texto))
# print(re.findall(r'\D+', texto))
# print(re.findall(r'\s+', texto))
# print(re.findall(r'\S+', texto))
# print(re.findall(r'\be\w+', texto)) # Procuro apenas palavras que tem na borda inicial 'e'
# print(re.findall(r'\w+e\b', texto)) # Procuro apenas palavras que tem na borda final em 'e'
# print(re.findall(r'\b\w{4}\b', texto)) # Procura palavras de 4 letras, com borda para ser somente palavras
# print(re.findall(r'\w{4}', texto)) # se não tiver borda, vai pegar as primeiras 4 de TODAS as palavras
print(re.findall(r'flo\B', texto)) # pega todos os 'flo' do texto que não sejam somente flo