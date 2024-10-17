import os
# import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'Pasta do Zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'arquivos_compactados.zip'  # Criando caminhos de arquivos # noqa 501
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'Desempacotando com Pyhton'

# shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True) # Deletenado pastas com shutil # noqa 501
# Path.unlink(CAMINHO_COMPACTADO, missing_ok=True) # Deletando arquivos com Path # noqa 501
# shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True) # noqa 501
# shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)  # Se ja existir não quebra o código


def criar_arquivos(qtd: int, zip_dir: Path):  # Função que recebe qnt de arquivos e algum diretório # noqa 501
    for i in range(qtd):
        texto = 'arquivo_%s' % i  # Renomeando cada arquivo com interpolação, arquivo_ + 1 -> string # noqa 501
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:  # Crinado arquivo txt # noqa 501
            arquivo.write(texto)  # Escrevendo no arquivo texto


criar_arquivos(10, CAMINHO_ZIP_DIR)

'''Criando zip'''
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:  # Criando um arquivo zip
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):  # Pegando os dados da pasta caminho_zip_dir com os.walk() # noqa 501
        for file in files:
            zip.write(os.path.join(root, file), file)  # Escrevendo(write) em zip - E salvando em modo file(somente arquivos) # noqa 501
            #         os.path.join-adicionando(diretorio, arquivo)

with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:  # Exibindo arquivo do meu zip
    for arquivo in zip.namelist():  # Exibi arquivos dentro de um zip
        print(arquivo)

with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:  # Exibindo arquivo do meu zip
    zip.extractall(CAMINHO_DESCOMPACTADO)  # extractall para desenpacotar(em determinada pasta=CAMINHO_DESEMPACOTADO) # noqa 501
