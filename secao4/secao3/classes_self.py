# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.


class Carro: # Uma classe pode gerar várias instâncias. (linha15, linha21)
    def __init__(self, nome): # Self se referencia ao próprio objeto criado (linha15, linha21)
        self.nome = nome 
# Classe - Molde (geralmente sem dados)
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca') # Instância da class (objeto) - Tem os dados
fusca.acelerar()
Carro.acelerar(fusca) # Class, Método e argumento
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta) # Class, Método e argumento
# print(celta.nome)