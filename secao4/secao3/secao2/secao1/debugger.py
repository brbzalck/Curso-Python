# if / elif      / else
# se / se não se / se não

condicao1 = False
condicao2 = True
condicao3 = False
condicao4 = False

if condicao1: # sempre começa com o IF
    print('Código para condição 1')
    print('Código para condição 1') # pode colocar mais de uma linha em cada if ou elif
elif condicao2: # ELIF caso precise de mais de uma verificação
    print('Código para condição 2') 
elif condicao3:
    print('Código para condição 3') # IF ELIF E ELSE representa um bloco que se verificado true na primeira oportunidade se encerra
elif condicao4:
    print('Código para condição 4')
else: # ELSE para finalizar as verificações, caso nenhuma seja satisfeita = else
    print('Nenhuma condição foi satisfeita.')

print('fim do código :D')