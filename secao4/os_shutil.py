# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os
import shutil

HOME = os.path.expanduser('~')  # Pegando caminho usuário do pc
DESKTOP = os.path.join(HOME, 'Desktop')  # Adicionando Desktop ao caminho base
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Modelos Editora')  # Criando caminho pasta Original # noqa 501
NOVA_PASTA = os.path.join(DESKTOP, 'Nova Pasta')  # Criando caminho da nova pasta # noqa 501

os.makedirs('Nova Pasta', exist_ok=True)  # Criando de fato a pasta(makedirs), se já existir exist_ok=não quebra # noqa 501

'''Criando subdiretórios da PO na Nova Pasta'''
for root, dirs, files in os.walk(PASTA_ORIGINAL):  # Pegando pasta diretórios e arquivos da pasta original # noqa 501
    for dir_ in dirs:  # Para cada subdiretório da PO
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)  #Substitui diretório para Nova pasta(repleace) # noqa 501
        #                                                                               dir_ adiciona subdiretório # noqa 501
        os.makedirs(caminho_novo_diretorio, exist_ok=True)  # Cria novo diretório com subdiretório de PO em Nova Pasta # noqa 501

    '''Criando caminho do arquivo e o arquivo em si na Nova Pasta'''
    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)  # Pegando o caminho do arquivo # noqa 501
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file_)  #Substitui diretório para Nova pasta(repleace) # noqa 501
        #                                                                             e adiciona arquivo ao novo diretório # noqa 501
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)  # Copinado o arquivo DE FATO # noqa 501