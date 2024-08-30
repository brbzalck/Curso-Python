# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Modelos Editora')
NOVA_PASTA = os.path.join(DESKTOP, 'Nova Pasta')

'''rmtree exclui permanentemente, **não fica na lixeira**'''
shutil.rmtree(NOVA_PASTA, ignore_errors=True) # Exemplo de como se deleta uma pasta
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA) # Exemplo de como se copia uma pasta
shutil.rmtree(NOVA_PASTA, ignore_errors=True) # Por fim apagando a pasta
