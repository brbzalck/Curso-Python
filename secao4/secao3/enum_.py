# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum # Módulo para numerar grupo de coisas

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])


class Direcoes(enum.Enum): # Criando uma classe de direções que herda enum.Enum(no caso irei numerar direções)
    ESQUERDA = enum.auto() # Utilizando a classe 'auto' de enum para enumerar automatico
    DIREITA = 2
    ACIMA = enum.auto()
    ABAIXO = 'Pode ser str tbm'


print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA) # Jeitos de chamar a chave em enum
print(Direcoes(1).name, Direcoes.ESQUERDA.value) # Chamando chave e valor


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes): # Verificando se direcao é instancia de Direcoes
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})') # Chave valor


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
