# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

''''____________________________________________________________________________________________'''



''''____________________________________________________________________________________________'''
# Passando o caminho da pasta aonde quero salvar o arquivo
caminho = 'C:\\Users\\zero\\Desktop\\Criando arquivo com Python\\' 
caminho += 'ArquivoCriado.txt' # concatenando o arquivo criado na pasta


#with open(caminho concatenado, 'método') as VAR:
with open(caminho, 'w') as arquivo:
    arquivo.write('Pó olhar que criou')

''''____________________________________________________________________________________________'''

with open(caminho, 'w+') as arquivo: # utilizando o w+ para escrever e ler
    arquivo.write('Linha 1\n') # escrevendo linha 1 no arquivo, e quebrendo a linha
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n') # escrevendo mais de uma coisa por meio de uma tupla
    )
    arquivo.seek(0, 0) # voltando ao começo do arquivo
    print(arquivo.read()) # lendo o arquivo até agr
    print('Lendo')
    arquivo.seek(0, 0) # voltando ao começo denovo(exibi novamente)
    # print(arquivo.readline(), end='')
    # print(arquivo.readline().strip())
    # print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)  # voltando ao começo denovo(exibi novamente)
    for linha in arquivo.readlines(): # lendo as linhas de um arquivo
        print(linha.strip()) # exibindo linha por linha formatada em strip


print('#' * 10)

with open(caminho, 'r') as arquivo:
    print(arquivo.read()) # lendo arquivo

''''____________________________________________________________________________________________'''
# 'w' apaga oque tem no arquivo, e recomeça com os novos write
with open(caminho, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    
with open(caminho, 'a+') as arquivo:
    arquivo.write('Que doidera') # 'a' para adicionar ao arquivo, sem deletar os ja existentes

# os.remove(caminho_arquivo) # ou unlink # removendo arquivo
# os.rename(caminho_arquivo, 'aula116-2.txt') # renomeando arquivo