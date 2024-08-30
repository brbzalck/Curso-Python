# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC): # Sempre que a classe for abstrata, vai servir como modelo para subclasses de métodos
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod # Exemplo de modelo que vai ser usado na subclasse
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name) # Puxando método init da super class
        # print('Sou inútil')

    @AbstractFoo.name.setter # Usando o setter específico da classe abstrata(puxa tbm o getter)
    def name(self, name):
        self._name = name # Esse resultado sobe para getter


foo = Foo('Bar')
print(foo.name)