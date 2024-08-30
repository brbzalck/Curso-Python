# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

# Definindo argumento de entrada
parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela', # Exibi um help p qm executa
    # type=str, # Tipo do argumento
    metavar='STRING', # 
    # default='Olá mundo', # Valor padrão de argumento
    required=False, # Força um argumento
    action='append',  # Recebe o argumento mais de uma vez
    # nargs='+', # Recebe mais de um valor em uma lista
)

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs', # modulo.py -h -> Mostra um help do módulo
    action='store_true' # Consegue ver se é True ou False
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

print(args.verbose)