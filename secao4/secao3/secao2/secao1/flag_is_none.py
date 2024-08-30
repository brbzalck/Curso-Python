"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False # Caso seja falso, if da linha 13 e 17 executa
passou_no_if = None # Atribui um valor neutro e marca uma bandeira para variável dentro do cod.

if condicao:
    passou_no_if = True # Muda o valor da VAR passou_no_if
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None: # Caso a VAR condição for falsa, o valor da VAR passou_no_if continua None e prossegue no IF.
    print('Não passou no if')
else:
    print('Passou no if')