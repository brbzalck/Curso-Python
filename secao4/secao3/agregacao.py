# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).


class Carrinho:
    def __init__(self): # Lista vazia manipulação para produtos
        self._produtos = [] # Definindo produtos como private, para conseguir editar o atributo somente dentro da classe

    def total(self): # Função que soma o total
        return sum([p.preco for p in self._produtos]) # para cada produto em self._produtos > pega o preço dos produtos e sum

    def inserir_produtos(self, *produtos): # recebendo o objeto(carrinho), e os *produtos p1, p2 empacotados em uma tupla
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto) # Para cada produto dos meus produtos, adiciona produto a minha lista de manipulação

    def listar_produtos(self): # Recebo carrinho em self
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco) # Listando cada produto pelo nome e preco da minha lista de manipulação
        print()


class Produto:
    def __init__(self, nome, preco): # Classe produto recebe Objeto(p1,p2), nome e preco Produto(nome, preco)(linha40)
        self.nome = nome
        self.preco = preco
        

carrinho = Carrinho() # Criando um objeto para classe carrinho, para ter a possibilidade de usar os métodos da classe.

p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20) # Criando dois objetos para Classe Produto

carrinho.inserir_produtos(p1, p2) # Utilizando a instancia carrinho para manipular minha classe Carrinho
carrinho.listar_produtos()
print(carrinho.total())

