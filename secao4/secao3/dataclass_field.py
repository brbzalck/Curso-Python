# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str = field(default='Missing', repr=False)
    sobrenome: str  = 'Not Sent'
    idade: int = 0 #                se precisar definir como valor padrão um valor mutável utiliza default_factory
    enderecos: list[str] = field(default_factory=list) # Desse jeito, cada objeto vai ter sua própria lista de endereço

if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)