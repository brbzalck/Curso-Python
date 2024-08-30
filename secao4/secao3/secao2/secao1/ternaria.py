"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
IF E ELSE NA MESMA LINHA
"""
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor' # Se a condição for True = 'Valor', se não 'Outro valor'
# print(variavel)
digito = 9  # > 9 = 0
novo_digito = digito if digito <= 9 else 0 # se o Digito for menor ou igual a 9 == digito, se não == 0
novo_digito = 0 if digito > 9 else digito # (ao contrário) se o Digito for maior que 9 == 0, se não digito == digito
print(novo_digito)
print('Valor' if False else 'Outro valor' if False else 'Fim') # exemplo de if dentro de um if na mesma linha...
# se condição for falsa == 'Valor', se não 'Outro valor' se a condição for falsa, se não 'fim'