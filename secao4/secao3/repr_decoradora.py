def meu_repr(self):
    nome_classe = self.__class__.__name__ # pegando nome da classe
    obj_atr = self.__dict__ # Pegando os atributos do objeto
    class_repr = f'{nome_classe}{obj_atr}'
    return class_repr

# FUNÇÃO DECORADORA
def adiciona_repr(cls):
    cls.__repr__ = meu_repr # Redefinindo a função __repr__ pela minha própria função
    return cls # Retornando a classe modificada pelo meu_repr

# FUNÇÃO DECORADORA
def meu_planeta(metodo): # Decoradora recebe método
    def interna(self, *args, **kwargs): # Interna recebe esse objeto e argumento
        resultado = metodo(self, *args, **kwargs) # Jogando método(objeto, atributo) | falar_nome(terra, Terra)
        if 'Terra' in resultado: 
            return 'Você está em casa'
        return resultado
    return interna


@adiciona_repr # Sempre que criar um objeto, por meio dessa decoradora, vai representar o objeto
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr # Decorador ja pega o objeto instânciado
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'




brasil = Time('Brasil')
portugal = Time('Portugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)
print(terra.falar_nome())
print(marte.falar_nome())