# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código


# FUNÇÃO DENTRO DE CLASS == MÉTODO
class Carro:
    def __init__(self, nome): # Método da class Carro que inicia com __init__ recebendo o objeto em self, e o atributo nome
        self.nome = nome # self(fusca, celta).nome(atributo) = nome(argumento do método)

    def acelerar(self): # Método de class que recebe self(objeto) e exibi o nome do objeto + f'string'
        print(f'{self.nome} está acelerando...')


# string = 'Luiz'
# print(string.upper())

fusca = Carro('Fusca') # Criando um objeto na class Carro, com argumento de 'Fusca'
print(fusca.nome) # Exibindo o atributo nome de Fusca
fusca.acelerar() # Executando método de Carro .acelerar()

celta = Carro(nome='Celta') 
print(celta.nome)
celta.acelerar()