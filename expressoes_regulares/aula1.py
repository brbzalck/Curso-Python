import re

# findall, search, sub, compile

string = 'Este é um teste de expressões teste regulares.'
# re.search para usar o método de re(r'para procurar', variável contendo valores)
# search pega o primeiro match e devolve como objeto
print(re.search(r'teste', string))
# findall pega TODOS os finds e devolve numa lista
print(re.findall(r'teste', string))
# sub para trocar r'' por '' -> recebe 3 argumentos(find, subs, var)
print(re.sub(r'teste', 'ABCD', string, count=1))  # count(determinar qnts vezes substituir)

# compilando com compile para dentro de uma variável, a string desejada para procura/substituição
regexp = re.compile(r'teste')
# usar da variável, os métodos para procura/substituição
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string, count=1))