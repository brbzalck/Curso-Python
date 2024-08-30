# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome): # __call__ usando para conseguir executar o objeto
        print(nome, 'está chamdno', self.phone) # Fazendo manipulções quaiquer
        return 12345


call1 = CallMe('23945876545') 
call1('Luiz Otávio') # Executando objeto e jogando para uma VAR
