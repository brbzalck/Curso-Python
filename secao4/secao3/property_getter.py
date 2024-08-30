# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor): # Classe normal com método que recebe cor da caneta
        self.cor_tinta = cor 

    @property # Dentro do escopo da classe, @property se comporta como um método, mas no código cliente como atributo(linha 32)
    def cor(self): # Usado ao meu ver para redefinir nome de atributo, sem quebrar o código com o cliente
        print('PROPERTY')
        return self.cor_tinta # Em vez de self.cor, retorna self.cor_tinta
# pois self cor não existe mais

    @property # Método
    def cor_tampa(self):
        return 123456

###########################


caneta = Caneta('Azul')
print(caneta.cor) # Atributo
print(caneta.cor) # Atributo
print(caneta.cor) # Atributo
print(caneta.cor) # Atributo
print(caneta.cor) # Atributo
print(caneta.cor) # Atributo
print(caneta.cor_tampa) # Atributo

#####################################

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta

# ###########################


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())