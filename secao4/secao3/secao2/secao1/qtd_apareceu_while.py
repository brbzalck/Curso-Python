frase = 'O rato roeu a roupa do rei de roma'

i = 0 # Indice que começa com 0 (pega o primeiro item(letra) da str)
qtd_apareceu_mais_vezes = 0 # Reservado para letra que mais aparecer durante a execução do problema
letra_apareceu_mais_vezes = '' # str vazia para armazenar os resultados da iteração sobre a str

while i < len(frase): # Usado para verificar todas as letras com base no Indice
    letra_atual = frase[i] # coletando letras pelo indice que atualiza(linha 20)

    if letra_atual == ' ': # Tirando o espaço da contagem.
        i += 1
        continue

    qtd_atual = frase.count(letra_atual) #Contando quantas vezes a Letra atual apareceu

    if qtd_apareceu_mais_vezes <= qtd_atual: # se a letra que esta sendo verificada for maior, ela substitui as expressões abaixo
        qtd_apareceu_mais_vezes = qtd_atual # atualiza a quantidade que a Letra que apareceu mais vezes
        letra_apareceu_mais_vezes = letra_atual # atualiza a letra que apareceu mais vezes
#       atribuindo para as duas variáveis, qual letra e quantas vezes ela apareceu
    i += 1 # aumentando mais 1 no indice, para iterar até chegar no limite do len()

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)