from log import LogFileMixin # Importando funcionalidades de LogFileMixin

class Eletronico: # Classe recebe objeto e nome
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False # Flag = desligado

    def ligar(self): # Método para ligar
        if not self._ligado: # se estiver desligado liga
            self._ligado = True

    def desligar(self): # Metodo para desligar
        if self._ligado: # Se estiver ligado desliga
            self._ligado = False


# Herança multipla, Smartiphone child class de Eletronico, com outra class importada para atribuir funcionalidades
class Smartphone(Eletronico, LogFileMixin): 
    def ligar(self): # Assinatura do método
        super().ligar() # Pegando o metodo da super class

        if self._ligado: # se estiver ligado
            msg = f'{self._nome} está ligado' # Cria msg com nome do smartphone
            self.log_success(msg) # Utilizando a herança
            # Enviando objeto e msg para função log_success de LogFileMixin que foi importada

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)


    