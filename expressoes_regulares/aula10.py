import re
# 0.0.0.0 255.255.255.255
# 025.258.963-10 02525896310

# Teste essa expressão
# em https://regex101.com/r/lWVPOr/1


cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
# print(cpf_reg_exp.search(cpf))

''' PRIMEIRA MANEIRA DE VALIDAR IP '''

ip_reg_exp = re.compile(r'''
    ^
    (?:
        25[0-5] | # 250 - 255 OU
        2[0-4][0-9] | # 200 - 249
        1[0-9]{2} | # 100 - 199
        [1-9][0-9] | # 10 - 99
        [0-9] # 0 - 9
    ) # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto
    \. # \. para procurar esse find apenas no começo depois que terminar com "155."
    (?:
        25[0-5] | # 250 - 255 OU
        2[0-4][0-9] | # 200 - 249
        1[0-9]{2} | # 100 - 199
        [1-9][0-9] | # 10 - 99
        [0-9] # 0 - 9
    ) # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto
    \. # \. para procurar esse find apenas no começo depois que terminar com "155."
    (?:
        25[0-5] | # 250 - 255 OU
        2[0-4][0-9] | # 200 - 249
        1[0-9]{2} | # 100 - 199
        [1-9][0-9] | # 10 - 99
        [0-9] # 0 - 9
    ) # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto
    \. # \. para procurar esse find apenas no começo depois que terminar com "155."
    (?:
        25[0-5] | # 250 - 255 OU
        2[0-4][0-9] | # 200 - 249
        1[0-9]{2} | # 100 - 199
        [1-9][0-9] | # 10 - 99
        [0-9] # 0 - 9
    ) # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto
    $
    # flag re.X para poder comentar dentro da expressão
''', flags=re.X)

''' SEGUNDA MANEIRA DE VALIDAR IP '''

ip_reg_exp = re.compile(r'''
    ^
    (?: # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto                   
        (?:
            25[0-5] | # 250 - 255 OU
            2[0-4][0-9] | # 200 - 249
            1[0-9]{2} | # 100 - 199
            [1-9][0-9] | # 10 - 99
            [0-9] # 0 - 9
        ) # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto
        \. # \. para procurar esse find apenas no começo depois que terminar com "155."
    ){3}
        (?:
            25[0-5] | # 250 - 255 OU
            2[0-4][0-9] | # 200 - 249
            1[0-9]{2} | # 100 - 199
            [1-9][0-9] | # 10 - 99
            [0-9] # 0 - 9
        )$ # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto
            
''', flags=re.X)

''' TERCEIRA MANEIRA DE VALIDAR IP '''

ip_reg_exp = re.compile(r'''
    ^
    (?: # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto                   
        (?:
            25[0-5] | # 250 - 255 OU
            2[0-4][0-9] | # 200 - 249
            1[0-9]{2} | # 100 - 199
            [1-9][0-9] | # 10 - 99
            [0-9] # 0 - 9
        ) # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto
        \.? # \. para procurar esse find apenas no começo depois que terminar com "155."
    ){4}
    \b
    $ # Como não tem grupo de captura, o resultado aqui é apenas o "match" da expressão com o texto
            
''', flags=re.X)


''' VERSÃO COMPCTA DE VALIDAR IP '''

# DEBUG DELA ESTÁ DESCRIMINADA NOS MODOS DE VALIDAÇÃO ACIMA
ip_reg_exp = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))