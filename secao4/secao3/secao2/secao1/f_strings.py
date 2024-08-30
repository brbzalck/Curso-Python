nome = 'Lucas'
altura = 1.73
peso = 60
imc = (60 / 1.73) / 1.73


#   f-strings - Usado para formatar determinada linha, Ex: f'{nome da variável} str {nome da variável} str'
linha_formatada = f'{nome} tem {altura} de altura, pesa {peso} kg e seu imc é = {imc:.2f}.'
print(linha_formatada)