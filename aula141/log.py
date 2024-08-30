from pathlib import Path # Classe responsável por achar o caminho do arquivo
LOG_FILE = Path(__file__).parent / 'log.txt' 

class Log: # super class é usado para fornecer atributos e métodos para as subclasses
    def _log(self, msg): 
        raise NotImplementedError('Implemente o método') # se tentar executar minha super classe quebra o código
    
# Criando na super class métodos para serem utilizados pelas child class
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    # retornando a execução do método _log de LogPrintMixin + (Success: Qualquer Coisa)
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
        
class LogPrintMixin(Log):
    def _log(self, msg): # recebe objeto(l) + msg formatada
        print(f'{msg} ({self.__class__.__name__})') # Exibe msg + nome da classe do objeto(self)

# Sempre que ver 'Mixin' será utilizado para adicionar método etc
class LogFileMixin(Log): 
    def _log(self, msg):
        print(msg) # Msg formatada pelo método da superclass
        msg_formatada = f'{msg} ({self.__class__.__name__})' # Concatenando msg com nome da classe do objeto
        print('Salvando no log', msg_formatada) # Concatenando mais uma vez 'str', msg_formatada
        with open(LOG_FILE, 'a') as arquivo: # Adicionando arquivos com 'a'
            arquivo.write(msg_formatada) # adicionando em arquivo msg formatada :P
            arquivo.write('\n')

if __name__ == '__main__':
    lp = LogPrintMixin() # Criando um objeto na child class
    lp.log_success('Logado com sucesso') # utilizando um metodo da superclass no objeto da childclass
    lp.log_error('Loged error?')
    lf = LogFileMixin()
    lf.log_success('Salvo com sucesso')
    lf.log_error('Saved error')
