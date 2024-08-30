# Problema dos parâmetros mutáveis em funções Python

# SEMPRE QUE FOR DEFINIR PARAMETROS MUTÁVEIS, ATRIBUA = None
def adiciona_clientes(nome, lista=None): # para não ter o problema de ter sempre a mesma lista na função
    if lista is None: # Se não mandar a lista como argumento
        lista = [] # Cria uma lista nova que será o nome da VAR que chamou a função
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)