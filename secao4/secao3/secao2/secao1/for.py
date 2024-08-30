# senha_salva = '123456'
# senha_digitada = '' # str vazia reservada para iteração da str
# repeticoes = 0 # para contar a qnt de vezes que o codigo rodou

# while senha_salva != senha_digitada: # se a senha_salva for diferente de senha digitada, fim do programa
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ') # solicita a senha e controla a partir do 0 qual tentativa de senha esta

#     repeticoes += 1 # sobe mais 1 no indice, para mudar em qual tentativa esta

# print(repeticoes) # mostra qnts tentativas foram
# print('Aquele laço acima pode ter repetições infinitas') # prova que pode ter infinitas repetições, dependendo do Usuário no caso


texto = 'Python' # str a ser iterada

novo_texto = '' # str vazia para guardar o valor da iteração linha18
for letra in texto: #for = PARA CADA / letra = (Variável criada para jogar itens da Var iterada) in = em / texto = (Variável que esta sendo iterada) :
    novo_texto += f'*{letra}' # Crinda um novo texto, começando com * e letra que foi iterada com for
    #print(letra) 
print(novo_texto + '*') # exibindo o novo_texto depois de completamente iterado e modificado, e adicionando um * no final p ficar bonitin

#  FOR É MAIS USADO QUANDO É POSSÍVEL SABER QUANTAS REPETIÇÕES VÃO EXISTIR NA ITERAÇÃO