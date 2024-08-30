# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

lista_tarefas = [] # Listas de manipulação
refazendo = [] 

while True: # enquanto

    print('Comandos: listar, desfazer ou refazer.')
    entrada = input('Digite um comando acima ou adicione uma tarefa: ')
    print()

    def comandos(entrada): # função que recebe comandos
        if entrada == 'listar':
            print(lista_tarefas)
        elif entrada == 'desfazer':
            try:
                refaz = lista_tarefas.pop() # Tirando da lista oficial
                refazendo.append(refaz) # Jogando p lista lixeira
            except IndexError: # Usando except para caso não haja mais items para desfazer
                print()
                print('Nada para desfazer',)
                print()
        elif entrada == 'refazer':
            try:
                atualizada = refazendo.pop() # Tirando da lista lixeira
                lista_tarefas.append(atualizada) # Jogando p lista oficial
            except IndexError: # Usando except para caso não haja mais items para refazer
                print()
                print('Nada para refazer :p')
                print()
        else:
            lista_tarefas.append(entrada) # Caso nenhum dos comando for TRUE, adiciona o input p lista oficial




    comandos(entrada) # Chama a função
