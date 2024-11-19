# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

####################################### MEU JEITO

# pergunta1 = perguntas[0]


# print(pergunta1['Pergunta'])
# print()
# opcoes = pergunta1['Opções']

# print(f'a)', opcoes[0], f' \nb)', opcoes[1], f' \nc)', opcoes[2], f' \nd)', opcoes[3])

# resposta = input('Escolha uma opção:')

# if resposta != 'c':
#     print('Resposta errada.')
# else:
#     print('Resposta certa.')
# print()
# pergunta2 = perguntas[1]

# print(pergunta2['Pergunta'])
# opcoes2 = pergunta2['Opções']

# print('a)', opcoes2[0], '\nb)', opcoes2[1], '\nc)', opcoes2[2], '\nd)', opcoes2[3])

# resposta2 = input('Escolha uma opção: ')

# if resposta2 != 'a':
#     print('Resposta errada.')
# else:
#     print('Resposta certa.')
# print()

# pergunta3 = perguntas[2]

# print(pergunta3['Pergunta'])
# opcoes3 = pergunta3['Opções']

# print(f'a) {opcoes3[0]} \nb) {opcoes3[1]} \nc) {opcoes3[2]} \nd) {opcoes3[3]}')

# resposta3 = input('Escolha uma opção: ')

# if resposta3 != 'b':
#     print('Resposta errada: ')
# else:
#     print('Resposta certa. ')

# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0 # Variável para contar a qnt de acertos
for pergunta in perguntas: # iterando minha lista perguntas para a VAR pergunta
    print('Pergunta:', pergunta['Pergunta']) # exibindo por meio da VAR pergunta a chave 'Pergunta'
    print() # pulando linha

    opcoes = pergunta['Opções'] # Variável para armazenar a chave opções da minha pergunta em específico
    for i, opcao in enumerate(opcoes, start=1): # para cada índice e opção das minhas opções(enumerate para usar o i como enumerador)
        print(f'{i})', opcao) # exibi na tela o índice da opção com a opção em si
    print() # pula linha

    escolha = input('Escolha uma opção: ') # segurando o programa até que o usuário digite a entrada

    acertou = False # flag para caso erre(linha115)
    escolha_int = None # flag para caso o usuário não digite um número inteiro(linha106-107-109)
    qtd_opcoes = len(opcoes) # Var guarda a qtd de opções

    if escolha.isdigit(): # Verificando se a resposta do usuário é digito
        escolha_int = int(escolha) - 1 # caso não seja, VAR escolha_int continua NONE, e executa linha 118

    if escolha_int is not None:  # se o número for digito, então escolha_int converte inteiro e deixa de ser none executando o if da linha
        if escolha_int >= 0 and escolha_int < qtd_opcoes: # se escolha não estiver entre os índices 0 a qnt_opcoes(len(opcoes))
            if opcoes[escolha_int] == pergunta['Resposta']: # E SE TBM dentro das minhas opções [e índice obtido] == resposta predefinida
                acertou = True # acertou = True executa linha 115

    print()
    if acertou: 
        qtd_acertos += 1 # contando o número de acertos
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos) # Mostra a qnt de acertos contabilizados em linha 116
print('de', len(perguntas), 'perguntas.')