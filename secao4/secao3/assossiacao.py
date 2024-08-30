# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome) -> None: # Classe escritor __init__ recece Objeto(escritor) nome (luiz)
        self.nome = nome # escritor.nome = 'Luiz'
        self._ferramenta = None # Definindo o atributo protected > ._ferramenta

    @property # Gerando meu gett
    def ferramenta(self): # Ferramenta recebe escritor
        print('b')
        return self._ferramenta # retorna(linha24)

    @ferramenta.setter # setando ferramenta
    def ferramenta(self, ferramenta): # recebe Objeto(escritor) ferramenta
        print('a')
        self._ferramenta = ferramenta # ferramenta agora é representada por escritor._ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')

escritor.ferramenta = maquina_de_escrever

# print(caneta.escrever())
# print(maquina_de_escrever.escrever())

print(escritor.ferramenta.escrever())
