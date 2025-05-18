uma_string: str = 'Um valor'
um_inteiro: int = 123456
um_flutuante: float = 1.6
um_boleeano: bool = True
um_set: set = {1, 2, 3}
uma_lista: list = [1, 2, 3]
uma_tupla: tuple = (1, 2, 3)
um_dict: dict = {}

uma_string = '1'

# tipando um método
def soma(x: int, y: int, z: float) -> float:
    return x + y + z

# definindo que tipo de dados tem dentro das minhas listas
lista_inteiros: list[int] = [1, 2, 3, 4]
lista_strings: list[str] = ['1', '2', '3', '4']
lista_tuples: list[tuple] = [('1', '2'), ('3', '4')]
lista_lista_int: list[list[int]] = [[1, 2], [3, 4]]

# definindo oque contem no meu dict > str para chave & int para valor
um_dict_comun: dict[str, int] = {
    "A": 1,
    "B": 2,
    "C": 3,
}

# definindo oque contem no meu dict > str para chave & int para valor
um_dict_de_inteiros: dict[str, list[int]] = {
    "A": [1, 4],
    "B": [2, 5],
    "C": [3, 6],
}

# tipando meu set que contem inteiros
um_set_de_inteiros: set[int] = {1, 2, 3}

ListaInteiros = list[int]
DictListaInteiros = dict[str, ListaInteiros]

um_dict_de_listas: DictListaInteiros = {
    "A": [1, 4],
    "B": [2, 5],
    "C": [3, 6],
}

string_e_inteiros: str | int = 1 # Union
string_e_inteiros = 'a' # sem erros
string_e_inteiros = 1 # sem erros
lista_str_int: list[str | int] = [1, 2, 3, 'a']

# função de soma que recebe x int, y float OU none
def soma_none(x: int, y: float | None = None) -> float:
    # se o Y for instancia de float ou int
    if isinstance(y, float | int):
        return x + y
    return x + x


soma_none(1, 2)

from collections.abc import Callable

# função que recebe dois parâmetros e retorna um terceiro
SomaInteiros = Callable[[int, int], int]

# função que executa outra função somente de 2 inteiros com retorno de 1 inteiro
def executa(func: SomaInteiros, a: int, b: int) -> int:
    # retorna a execução da própria função que recebeu
    return func(a, b)

def soma_callable(a: int, b: int) -> int:
    return a + b


from typing import TypeVar

# para tipar dinamicamente
T = TypeVar('T')

# Uma lista onde os valores são dinâmicos(automáticos), index para selecionar valor da lista
def get_item(list: list[T], index: int) -> T:
    return list[index]

list_int = get_item([1, 'a', 3], 1)

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"
    
# definindo person como tipo de Person, para ter acesso aos métodos
def say_my_name(person: Person) -> str:
    return person.full_name

print(say_my_name(Person("John", "Doe")))