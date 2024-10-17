# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('/Users', 'zero', 'Desktop', 'visualg3.0.7')  # Criando caminho # noqa 501

for pasta_arquivo in os.listdir(caminho):  # Pegando as pasta_arquivos do caminho # noqa 501
    caminho_completo_pasta = os.path.join(caminho, pasta_arquivo)  # Adcionando pasta_arquivos em novo caminho # noqa 501
    print(pasta_arquivo)

    if not os.path.isdir(caminho_completo_pasta):  # se não for diretório, continue=ignore # noqa 501
        continue

    for arquivo in os.listdir(caminho_completo_pasta):  # para cada arquivo do caminho da pasta # noqa 501
        print('  ', arquivo)
