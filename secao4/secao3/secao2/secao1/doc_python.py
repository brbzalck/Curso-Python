"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000' # str, int, bool e float sao imutáveis
outra_variavel = f'{string[:3]}ABC{string[4:]}' # para mudar é necessário atribuir a outra VAR para tal. fino senores kkk
# print(string)
# print(outra_variavel)
print(string.zfill(10)) # tipo de método