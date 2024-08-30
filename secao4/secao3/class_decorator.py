
# Criando uma classe decoradora
class Conta:
    def __init__(self, multiplicador): # Que inicia com self(None) e multiplicador(5)(linha14)
        self.multiplicador = multiplicador # A partir daqui criase o objeto multiplicador(5)
        print(vars(self))

    # __call__ permite executar um objeto(callable)
    def __call__(self, func): # Recebe self(multiplicador=5)linha14 e a função numeros em si
        def interna(*args, **kwargs): # Empacotando tudo que receber
            print(vars(self))
            resultado = func(*args, **kwargs) # Usando a função numeros em meus argumentos e salvando numa variável
            return resultado * self.multiplicador # Multiplicando o resultado da função com o Multiplocador(linha5)
        return interna
        
@Conta(5) # Classe decoradora com 5 como atributo e multiplicador com objeto
def numeros(x, y):
    return x + y

calculadora = numeros(1, 4)
print(calculadora)




