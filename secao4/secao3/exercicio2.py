class Carro:
    def __init__(self, nome): # Classe carro com atributos nome, motor e fabricante
        self.nome = nome # Public
        self._motor_carro = None # Private
        self._fabricante_motor = None # Private

    @property
    def motor(self): # Recebe objeto carro
        return self._motor_carro # Retorna o valor setado no setter

    @motor.setter # Recebo como objeto self == gol(linha32) self == civic(linha41)
    def motor(self, valor):# O VALOR == Objeto de Motor / Fabricante
        self._motor_carro = valor # Definindo motor do carro = Volkswagen(Objeto de Motor == Valor)

    @property
    def fabricante(self):
        return self._fabricante_motor

    @fabricante.setter 
    def fabricante(self, valor): 
        self._fabricante_motor = valor

class Motor:
    def __init__(self, motor_nome): # Classe que recebe um objeto e nome de objeto
        self.nome = motor_nome

class Fabricante:
    def __init__(self, f_nome): # Classe que recebe um objeto e nome de objeto
        self.nome = f_nome


gol = Carro('Gol G5')
marca = Fabricante('Volkswagem')
motor1_0 = Motor('1.0 VHT') # Criando um objeto da classe Motor

gol.fabricante = marca
gol.motor = motor1_0 # MOTOR1_0 VAI SUBIR COMO ARGUMENTO PARA O SETTER
print(gol.fabricante.nome, gol.nome, gol.motor.nome)
print()

civic = Carro('Civic Modelo antigo')
marca = Fabricante('Honda') # Criando um objeto da classe Fabricante
motor1_8 = Motor('1.8 VHT')

civic.fabricante = marca # MARCA VAI SUBIR COMO ARGUMENTO PARA O SETTER
civic.motor = motor1_8 


# Exemplo de agregação, ja que carro agrega Fabricante e motor
print(gol.fabricante.nome, civic.nome, civic.motor.nome)
print()

'''________________________________________________________________________________________________________________________________________________________________________________'''

# class Carro:
 
#     def __init__(self, nome):
#         self.nome = nome
    
#     def motor_carro(self, m1):
#         print(f'{self.nome} tem o motor {m1.nome}')
    
#     def fabricante_carro(self, f1):
#         print(f'{self.nome} foi fabricado por {f1.nome}')
    
# class Motor:
 
#     def __init__(self, nome):
#         self.nome = nome
    
# class Fabricante:
 
#     def __init__(self, nome):
#         self.nome = nome
        
# carro1 = Carro("Celta")
# carro2 = Carro("Cruze")
# carro3 = Carro('Gol G5')
# motor1 = Motor("V6 1.0")
# motor2 = Motor('1.0 VHT')
# fabricante1 = Fabricante("Chevrolet")
# fabricante2 = Fabricante('Volkswagen')
 
# carro1.motor_carro(motor1)
# carro2.fabricante_carro(fabricante1)
# carro2.motor_carro(motor1)
# carro3.fabricante_carro(fabricante2)
# carro3.motor_carro(motor2)

'''____________________________________________________________________________________________________________________________________'''

class Cpu:
    def __init__(self, nome): #
        self.nome = nome
        self._placavideo = None
        self._memoria = None


    @property
    def memoria(self): # Recebe como objeto self(computador1)
        return self._memoria # Obtendo o valor de 'memoria'

    @memoria.setter
    def memoria(self, valor): 
        self._memoria = valor 

    @property
    def placavideo(self): 
        return self._placavideo 

    @placavideo.setter
    def placavideo(self, valor): # Recebe como objeto self(computador1)
        self._placavideo = valor # Setando o valor de placavideo

class PlacaVideo:
    def __init__(self, nome): # Classe que recebe  e guarda o nome da Placa de Video
        self.nome = nome

class Memoria:
    def __init__(self, nome): # Classe que recebe e guarda nome de Memoria
        self.nome = nome

computador1 = Cpu('Positivo') 
placa = PlacaVideo('Rx 580') # Jogando a função PlacaVideo(Argumento) para dentro da VAR 'placa'
qtd_memoria = Memoria('Memoria 16gb')

computador1.placavideo = placa # Passando o valor de placa(linha122) para computador1.placavideo 
computador1.memoria = qtd_memoria #                                       #objeto  /  #property 


######## EXEMPLO DE AGREGAÇÃO ##########
# JA QUE O CPU AGREGA UMA PLACAVIDEO E MEMORIA
print(computador1.nome, computador1.placavideo.nome, computador1.memoria.nome)
