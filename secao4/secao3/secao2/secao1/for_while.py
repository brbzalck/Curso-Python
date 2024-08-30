for i in range(10): # Vai rodar de 0 até 9
    if i == 2:
        print('i é 2, pulando...') 
        continue # Quando o I == 2, volta ao começo do for

    if i == 8:
        print('i é 8, seu else não executará')
        break # Quando o I == 8, termina o programa aqui

    for j in range(1, 4): # Determina a quantidade de vezes o I (0-linha) repete com J (1,2,3-coluna) (1, 4 = 3 vezes)
        print(i, j) # Termina o looping de J (3 vezes) e volta ao FOR inicial
else: # Só executa se eu remover o if-break da linha 6-8
    print('For completo com sucesso!') 