class Cliente:
    def __init__(self, nome): # método inicializador recebe Objeto e Nome
        self.nome = nome
        self.enderecos = [] # Lista vazia para manipulação dentro da minha classe

    def inserir_endereco(self, rua, numero): # método recebe Objeto Rua Numero
        self.enderecos.append(Endereco(rua, numero)) # Criando um objeto da Classe Endereco, dentro da classe cliente(composição)

    def inserir_endereco_externo(self, endereco): # método recebe objeto e endereço
        self.enderecos.append(endereco) 
# Exemplo de agregação(endereço vem externo), pois não depende inteiramente da Classe cliente, como visto na linha7
    def listar_enderecos(self): 
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)
# Exemplificando, que se deletar nome do Objeto de composição('Maria') os dependentes também vai junto (endereços)
### COMPOSIÇÃO ###

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente2 = Cliente('Lucas')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)

endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)

endereco_externo2 = Endereco('Av Doidera', 346)
cliente2.inserir_endereco_externo(endereco_externo2)

cliente1.listar_enderecos()

del cliente1


print(endereco_externo.rua, endereco_externo.numero)
print('######################## AQUI TERMINA MEU CÓDIGO')