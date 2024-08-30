# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...

class MyOpen: # Meu próprio save
    def __init__(self, caminho_arquivo, modo): # Inicia com self(MyOpen), caminho e modo
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None 

    def __enter__(self): # Quando abrir o arquivo
        print('Abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_excpetion, exception_, traceback_): # Quando fechar
        print('Fechando arquivo')
        # print(class_exception)
        # print(exception_) # Esses argumentos podem ser utilizados para informar um erro
        # print(traceback_)
        self._arquivo.close() # Usando a flag que armazenou open para fechar com .close


with MyOpen('Meu Save', 'w') as arquivo: # MyOpen é o próprio self para classe
    arquivo.write('Teste1\n') # Escrevendo no arquivo
    arquivo.write('Teste2\n') # Posso mudar a lógica de save dentro da classe criada por mim
    arquivo.write('Teste3\n')
    print('WITH', arquivo) 

    