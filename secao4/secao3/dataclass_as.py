from dataclasses import dataclass, asdict, astuple
# Métodos que transformam o objeto em dict ou tupla


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

if __name__ == '__main__':
    p1 = Pessoa('Lucas', 'Barbosa')
    print(asdict(p1))
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(astuple(p1))