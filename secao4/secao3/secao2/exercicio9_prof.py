import os # Modulo para limpar o terminal
import json

# DEFININDO FUNÇÕES FORA DO WHILE
def listar(tarefas):
    print()
    if not tarefas: # if not tarefas = falsy. Se a lista estiver vazia(falsy) faz a condição virar true
        print('Nenhuma tarefa para listar')
        return # Se sim encerra função

    print('Tarefas:') # 
    for tarefa in tarefas: # Exibindo tarefa linha por linha
        print(tarefa)
    print()


def desfazer(tarefas, tarefas_refazer): # Recebe as duas listas(lista atual, lista lixeira)
    print()
    if not tarefas: # se a lista tarefas estiver vazia retorna(falsy), tornando a condição verdadeira
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop() #  desfazendo o ultimo item de tarefas e salvando na VAR tarefa
    print(f'{tarefa=} removida da lista de tarefas.') # Exibindo o item removido
    tarefas_refazer.append(tarefa) # adicionando a lista lixeira para armazenamento oportuno
    print()


def refazer(tarefas, tarefas_refazer): # recebendo minhas duas listas(linha51, 52)
    print()
    if not tarefas_refazer: # se tarefas_refazer estiver vazia == falsy tornando a condição verdadeira
        print('Nenhuma tarefa para refazer')
        return #  se sim encerra função

    tarefa = tarefas_refazer.pop() # excluindo o ultimo item da lista lixeira e salvando na VAR tarefa
    print(f'{tarefa=} adicionada na lista de tarefas.') # mostando qual item foi recuperado
    tarefas.append(tarefa) # adicionando tarefa excluida para lista de tarefas oficial
    print()


def adicionar(tarefa, tarefas): # função recebe tarefa especifica e lista de tarefa oficial
    print()
    tarefa = tarefa.strip() # Tirando os espaços do input tarefa
    if not tarefa: # se o input do usuário estiver vazio == falsy torando a condição verdadeira
        print('Você não digitou uma tarefa.') 
        return # Encerrando função caso verídico
    
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa) # Adicionando tarefa(input) em tarefas(lista oficial)
    print()

'''____________________________________________________________________________________________________________________________________________________________________________________'''

def ler(tarefas, caminho_arquivo):
    dados = [] # Lista vazia
    try: # Tentando ler (caso não exista)
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: # Abrindo o arquivo para leitura pelo caminho do arquivo(linha72)
            dados = json.load(arquivo) # lendo o arquivo, e passando p variável dados
    except FileNotFoundError: # Caso ainda não exista o arquivo
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo) # Salva as tarefas no caminho do arquivo
    return dados # retorna lista


def salvar(tarefas, caminho_arquivo):
    dados = tarefas # passando as tarefas para lista vazia chamada dados
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: # Abrindo o arquivo para escrita, encoding para formatar namoral
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False) 
        # Salvando com dump - tarefas dentro do arquivo(linha67) identação de 2, formatação novamente
    return dados # retorna dados


CAMINHO_ARQUIVO = 'aula119.json' # Usado para passar como argumento para, def ler def salvar
tarefas = ler([], CAMINHO_ARQUIVO) # Variável que armazena valores da função e salva automaticamente no arquivo Json
tarefas_refazer = []

'''____________________________________________________________________________________________________________________________________________________________________________________'''

while True: #  Enquanto

    print('Comandos: listar, desfazer, refazer ou sair')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar': # se o input for listar
        listar(tarefas) # chamando minha função listar
        continue # Volta ao começo do while
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer) # Entregando como argumento minhas duas listas criadas
        listar(tarefas) # função listar
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer) # Entregando como argumento minhas duas listas criadas
        listar(tarefas) # função listar
        continue
    elif tarefa == 'clear':
        os.system('clear') # método system para limpar o terminal
        continue
    elif tarefa == 'sair':
        break
    else: # Caso não for comando vai cair aqui
        adicionar(tarefa, tarefas) # Jogando o input e a lista de tarefas para a função adicionar
        listar(tarefas) # tomale
        continue


salvar(tarefas, CAMINHO_ARQUIVO)