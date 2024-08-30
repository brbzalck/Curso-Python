"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal # Módulo decimal para calcular um número flutuante muito grande

numero_1 = decimal.Decimal('0.1') # caso queira um número pequeno converta para str (decimal.Decimal)
numero_2 = decimal.Decimal('0.7') # caso queira um número exatamente calculado deixe em int (decimal.Decimal)
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') # formatando o número com o :.2f
# numero_3 = 0.8
print(round(numero_3, 2)) # round usado para formatar o numero flutuante corretamente