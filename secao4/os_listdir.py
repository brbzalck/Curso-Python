# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('/Users', 'zero', 'Desktop', 'visualg3.0.7') # Criando caminho

for pasta_arquivo in os.listdir(caminho): # Pegando as pasta_arquivos do caminho
    caminho_completo_pasta = os.path.join(caminho, pasta_arquivo) # Adcionando pasta_arquivos em novo caminho
    print(pasta_arquivo)

    if not os.path.isdir(caminho_completo_pasta): # se não for diretório, continue=ignore
        continue

    for arquivo in os.listdir(caminho_completo_pasta): # para cada arquivo do caminho da pasta
        print('  ', arquivo)