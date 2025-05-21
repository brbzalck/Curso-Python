# https://regex101.com/r/W4kRV2/2/
# https://en.wikipedia.org/wiki/List_of_Unicode_characters

import re
senha_forte_regexp = re.compile(
    # garantindo que a verificação começe do começo da str
    r'^'
    # ?= lookahead para ver se existe qlqr algo que combine com essa condicional
    # . significa qualquer coisa dentro de determinada linha
    # * 0 ou mais vezes -> utilizado pois a verificação de 0 cobre se a letra minúscula estiver como primeiro carctere da senha
    # .* casa bem com lookahead para verificar se existe qualquer coisa do começo ao fim
    # [a-z] obriga qualquer letra minúscula
    r'(?=.*[a-z])'
    # igual a condicional anterior, só que agora com letra máiuscula(exige pelo menos 1 letra máiuscula)
    r'(?=.*[A-Z])'
    # igual a condicional anterior, só que agora com números(exige pelo menos um número)
    r'(?=.*[0-9])'
    # ?= lookahead para ver se existe qlqr algo que combine com essa condicional
    # .* verifica qualquer coisa até ela acabar(0 ou n)
    # [ -\/:-@[-`{-~] - adicionando caracteres especiais a condicional(exige pelo menos 1 caractere especial)
    r'(?=.*[ -\/:-@[-`{-~])'
    # . qualquer caractere
    # {12} a senha precisa ter 12 caracteres exatos
    r'.{12,}'
    # termina com 12 caracteres, nada mais
    r'$',
    # re.M -> multiline para analisar linha por linha
    flags=re.M
)

string = '''
VÁLIDAS
v2Ts7<o9T~}Y
j25TTbjJ:6{<
s`Mu6T;4M1!y
Li`hk6:3WX>3
d.D09}^dI2Vn

SEM MINÚSCULAS
I7^Y3RS^ 9]7
[P6W"83L5V{[
B7=;K8D6_}W5
1B_RT`93R%>1
EZU{7;2&D:64

SEM MINÚSCULAS E NÚMEROS
E}LV`C?X_G:{
AJH[@HD*V~=<
\A~AC{_V~MG 
W<-T}W:QAF'{
~YJ}|FILN>~)

SEM NÚMEROS CARACTERES E MINÚSCULAS
PBDZDPECUDNN
EJQWFWFFDEHY
XRCNLNRHYOZJ
TWIYPLWUDMNN
JMDTJSEPKVON

QUANTIDADE INVÁLIDA (6)
Iu4<1j
1x`P6g
@9t3Ry
qf9_6H
0o`9fO
'''

print(senha_forte_regexp.findall(string))