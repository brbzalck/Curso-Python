'''
For + Range
Range -> range(start, stop, step)

'''

numeros = range(0, 100, 2) # Começa em Zero/ vai até Cem/ e conta de Dois em Dois.
# numeros = range(100) Vai até 100
for numero in numeros: # PARA CADA (Var que criei para salvar a Var iterada) em (Var Iterada):
    print(numero) # Vai exibir na tela, começando do 0 até o 98, somente numeros pares(por conta do step que pula de 2em2)