# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯


# EM SUMA, SETTER SERVE PARA FILTRAR ATRIBUTOS COM LOGICA DE PROGRAMAÇÃO
class Caneta:
    def __init__(self, cor):
        self.cor = cor  # MÉTODO PRINCIPAL DA FUNÇÃO
        print('a')
        # private protected
        self._cor_tampa = None

# GETTER OBTEM VALOR, SETTER CONFIGURA O VALOR

    @property 
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor # exibindo o valor de setter(self._cor linha27), com o getter em si

    @cor.setter # Setando a cor da caneta
    def cor(self, valor): # setter recebe o nome do atributo e valor do atributo
        print('ESTOU NO SETTER') # o interessante é poder filtrar atributos aqui no meio
        self._cor = valor # Setando o valor da linha 38 em self._cor

    @property
    def cor_tampa(self):
        print('ESTOU NO GETTER') # Aqui eu uso o self._cor_tampa do meu set abaixo
        return self._cor_tampa

    @cor_tampa.setter # setando a cor tampa da caneta
    def cor_tampa(self, valor):
        print('ESTOU NO SETTER') # Aqui eu seto o valor em self._cor_tampa
        self._cor_tampa = valor


caneta = Caneta('Azul') # Executa primeiro em setter, depois em __init__
# caneta.cor = 'Rosa'
print(caneta.cor)
caneta.cor_tampa = 'Preta' # Definindo cor da tampa pelo set
print(caneta.cor_tampa) # Exibindo cor da tampa pelo get