# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('/Users', 'zero', 'Desktop', 'visualg3.0.7')  # Passando caminho do arquivo # noqa 501
counter = count()  # Contador que começa em 0

for root, dirs, files in os.walk(caminho):  # Para cada Diretório, Subdiretório e arquivos in OS.WALK # noqa 501
    the_counter = next(counter)  # Subindo 1 no contador
    print(the_counter, 'Pasta atual', root)  # Exibi contador atual, pasta = root # noqa 501

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)  # exibi contador atual, Sub diretório = dirs # noqa 501

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)  # Juntando diretório e arquivo # noqa 501
        print('    ', the_counter, 'FILE:', caminho_completo_arquivo)  # Contador atual com caminho completo arquivo(linha20) # noqa 501
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo
