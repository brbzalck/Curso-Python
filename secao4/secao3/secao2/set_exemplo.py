# Exemplo de uso dos sets

''' Usando set para guardar valores únicos mesmo que repetidos'''

letras = set() # crinado uma Variável do tipo set(vazia) para armazenar valores
while True: # Enquanto(programa não se encerra)
    letra = input('Digite: ') #  Pedindo uma letra ao usuário
    letras.add(letra.lower()) # .add armazenando ao set a letra do usuário, e convertendo para minúsculo.lower

    if 'l' in letras: # se l for a letra digitada(estiver nas letras armazenadas)
        print('PARABÉNS')
        break # encerra o programa

    print(letras) # Exibi na tela as letras digitadas