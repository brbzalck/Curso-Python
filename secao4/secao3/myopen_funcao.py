from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo # Pausa a execução, passando o controle para with com dados da variável arquivo
        
    # except Exception as e :
    #     print('Ocorreu um erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('Meu Save com Função', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
    print('With', arquivo)