# dir, hasattr e getattr em Python
# dir = verifica os métodos disponíveis para o tipo de dado pelo console debug
# hasattr verifica se existe
# getattr pegar um método de uma str
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo): # verificando se tem na minha string o método, método
    print('Existe upper') 
    print(getattr(string, metodo)()) # getattr na minha string, método()
else:
    print('Não existe o método', metodo)