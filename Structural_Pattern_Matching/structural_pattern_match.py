from dataclasses import dataclass


def execute_command(command):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ changing directory')
    else:
        print('$ command not implemented')

    print('...rest of the code')


# execute_command('pwd')

# BASIC
# case 'batata': = if case == 'batata':
# case _: == else (default case)


def execute_command2(command):
    # match = combinar, o command
    match command:
        # case = caso, o command for = 'ls'
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
            # case _ é o caso padrão, caso n tenho command
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('pwd')


# Commands in match
# match command_food.split(' '): # split two values
#     case ['like', food, ]: # get a literal and a variable

def execute_command3(command):
    # pegando o input recebido da func e JÁ executando o método split(separa str pelos espaços) em cima
    match command.split():
        # case que pega ls, caminho recebido separado pelo split, e tudo que vier dps separado
        case ['ls', path, *_]:
            # listando arquivos no caminho recebido
            print('$ listing files from', path)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('cd /Users/')

# Case with or inside a list
# case ['enjoy' | 'love', food]:


def execute_command4(command):
    # separando o input pelos espaços
    match command.split():
        # verifica se command é ls OU list, pega o caminho no índice 1 do split, mais tudo que vier depois empacotado
        case ['ls' | 'list', path, *_]:
            print('$ listing files from', path)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('list /home/ /Users /mais')

# With rest
# case ['like', *foods]


def execute_command5(command):
    # separando o input pelos espaços com split
    match command.split():
        # caso o cmd for ls OU list, e o resto do cmd empacotado como *directories
        case ['ls' | 'list', *directories]:
            # desempacotando cada diretório
            for directory in directories:
                print('$ listing directory from', directory)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')

# With case guard
# case ['like', *foods] if len(foods) <= 1:


def execute_command6(command):
    match command.split():
        # caso o cmd for ls OU list, com o resto do cmd empacotado em *directories
        # E SE esses diretórios empacotados for maior que 1 
        case ['ls' | 'list', *directories] if len(directories) > 1:
            # faz o desempacotamento/listagem
            for directory in directories:
                print('$ listing ALL directories from', directory)
        # caso o mesmo case de cima + SE os diretórios for menor/igual a 1
        case ['ls' | 'list', *directories] if len(directories) <= 1:
            # lista o único diretório
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('ls /one/')

# With as
# case data as variable if 'CRACKED' in variable:


def execute_command7(command):
    match command.split():
        # nomeando o cmd separado pelo split em the_command, nomeando a lista com [cmd, diretório] em the list
        case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
            # exibe o valor da variável no modelo var=valor, ex: the_command='ls'
            print(f'{the_command=}, {the_list=}')
        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('ls /one/')

# With generic placeholders
# case ['A', 'B', _, _]:
# case ['A', 'B', _, _, *_, 'Z']:


def execute_command8(command):
    match command.split():
        case ['ls' | 'list', _, *directories, _]:
            for directory in directories:
                print('$ listing ALL directories from', directory)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('ls /one/')

# With dicts
# case {'name': _, 'last': 'Doe'}:
# case {'name': 'Otávio' as name, 'last': 'Doe'} as data:


def execute_command9(command):
    match command:
        # case com dict, caso o input venha 'ls' casa com command
        # e em directories o primeiro valor separado por virgula é o path que pode ser UM ou VARIOS
        case {'command': 'ls', 'directories': [_, *_]}:
            # para cada diretório em ls[directories]
            for directory in command['directories']:
                print('$ listing ALL directories from', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command({'command': 'ls', 'directories': []})
# execute_command('ls /one/')

# With objects
# case Food(name='rice') | Food(name='banana'):


@dataclass
class Command:
    # a classe herdada de dataclass, tem o command que é uma string, e directories que é uma lista de str
    command: str
    directories: list[str]

# definindo um método que é do tipo Command
def execute_command10(command: Command):
    match command:
        # caso Command(receba instancia='ls', e diretório podendo ser um ou vários)
        case Command(command='ls', directories=[_, *_]):
            # pegando o atributo directories com command(self)
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


execute_command10(Command('ls', ['/users']))
execute_command10(Command('cd', ['/users']))