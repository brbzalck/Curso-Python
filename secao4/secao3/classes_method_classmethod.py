# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): # Método de instância(objeto)
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod # Método da classe para criar um objeto com User e Password
    def create_with_auth(cls, user, password):
        connection = cls() # Jogando a classe(executa) para VAR connection
        connection.user = user # Definindo um atributo user na minha Classe connection
        connection.password = password
        return connection # Retornando minha classe com os novos dados atribuidos para o objeto c1(linha33)

    @staticmethod
    def log(msg):
        print('LOG:', msg)


def connection_log(msg):
    print('LOG:', msg)


c1 = Connection.create_with_auth('luiz', '1234') # Crindo um objeto por meio de um método de Classe(com os argumentos previstos)
print(Connection.log('Essa é a mensagem de log')) # Exemplo de staticmethod(função dentro da classe)
print(c1.user) # Exibindo c1.user(linha20)
print(c1.password) # Exibindo c1.password(linha21)