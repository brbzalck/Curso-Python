nome = 'Lucas'
altura = 1.73
peso = 60
imc = (60 / 1.73) / 1.73


#   .format - Usado para formatar com a Função .format
#   Ex: nome_da_variavel = '{} str {} str {} str'
#       variavel_formatada = nome_da_variavel.format(a, b, c) A ordem das variáveis abc importa, e vai sair conforme os {} da str de cima.
saida = '{} tem {} de altura, pesa {} kg e seu imc é = {:.2f}.' # É utilizada ( :.2f ) para usar 2 Casas decimais dps da virgula
formato = saida.format(nome, altura, peso, imc)
print(formato)