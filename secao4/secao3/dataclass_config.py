from dataclasses import dataclass

@dataclass(repr=True) # Aqui configuro como dataclass se comporta
class Pessoa:
    nome: str
    sobrenome: str

if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome) # Ordenando lista por atributo(sobrenome) reverso
    print(ordenadas)