# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Utilizado para desmascarar quem é o objeto entre desenvolvedores
    def __repr__(self):
        class_name = type(self).__name__ # type(self).__name__ retorna o nome da classe
        return f'{class_name}(x={self.x!r}, y={self.y!r})'
    # !r é utilizado para representar de fato qual é o objeto
    
    # Método para somar atributos entre objetos(xp1 + xp2, yp1 + yp2)
    def __add__(self, other): # __add__ = + | recebe dois objetos(p1, p2)
        novo_x = self.x + other.x # somando o x de p1 com x de p2
        novo_y = self.y + other.y # somando o y de p1 com y de p2
        return Ponto(novo_x, novo_y) 

    # Método para ver qual dos dois objetos são maiores
    def __gt__(self, other): # __gt__ = > | recebe dois objetos(p1, p2)
        resultado_self = self.x + self.y # Somando x, y de p1
        resultado_other = other.x + other.y # Somando x, y de p2
        return resultado_self > resultado_other # p1 > p2?


if __name__ == '__main__':
    p1 = Ponto(4, 10)
    p2 = Ponto(6, 4)
#              10 14
    p3 = p1 + p2 # Jogando dois objetos para um só
    print(p3) # Representando meu objeto com __repr__

    print('P1 é maior que p2', p1 > p2) # Usando > como método(linha33)
    print('P2 é maior que p1', p2 > p1) # Para calcular a diferença entre objetos
