"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100: # Contando de 0 até 100
    contador += 1 # de 1 em 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue # Ignora o código pra baixo e volta no WHILE, trocando o print da linha 20
    #              pela linha 13 desse If, 
    
    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue # Ignora o código pra baixo, trocando o print da linha 20 pela linha 17

    print(contador)

    if contador == 40:
        break


print('Acabou')