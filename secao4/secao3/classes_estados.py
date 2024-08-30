# Mantendo estados dentro da classe

class Camera: # Definindo uma flag para o parâmetro filmando
    def __init__(self, nome, filmando=False): # filmando vai definir o estado do meu Objeto
        self.nome = nome # Definindo o nome de determinado objeto
        self.filmando = filmando # filmando=False na definição de objeto

    def filmar(self): # Função de filmar
        if self.filmando: # Se for True, exibi Já está filmando
            print(f'{self.nome} JÁ está filmando...')
            return # Fim da função
# Ou então se for False
        print(f'{self.nome} está filmando...') # Objeto está filmando
        self.filmando = True # Trocando filmando para True

    def parar_filmar(self): 
        if not self.filmando: # Se filmando for False
            print(f'{self.nome} NÃO está filmando...')
            return # Fim da função
# Ou se for True
        print(f'{self.nome} está parando de filmar...') 
        self.filmando = False # Trocando a Flag para False 

    def fotografar(self):
        if self.filmando: # True
            print(f'{self.nome} não pode fotografar filmando')
            return # Fim da função
# False
        print(f'{self.nome} está fotografando...')


c1 = Camera('Canon') # Crinado um objeto na classe Camera
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar() # Usando Métodos do meu Objeto c1
c1.parar_filmar()
c1.fotografar()

print()

c2.parar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar() # Usando métodos do meu Objeto c2
c2.parar_filmar()
c2.fotografar()