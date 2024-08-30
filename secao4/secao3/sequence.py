# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence # Sequence tem funcionalidades para criar minha própria lista

# Aula direcionada para cinto de ferramentas - Possíveis implementações na minha classe

class MyList(Sequence):
    def __init__(self):
        self._data = {} # Dados salvos em dict
        self._index = 0 # Atributo representando o índice
        self._next_index = 0

    def append(self, *values): # Método para adicionar, recebe valores desempacotados
        for value in values: # E para cada valor(quando adiciona mais de uma pessoa)
            self._data[self._index] = value # Adicionando índice para Items
            self._index += 1 # Sempre que adicionar alguem, sobe +1 no Len

    def __len__(self) -> int: # Qnt de dados na lista
        return self._index # Utilizando o index armazenado na (linha14)

    def __getitem__(self, index): # Linha(48)
        return self._data[index] # Objeto pega(chave) do dict Index[x] que armazena valor (Nome)(linha18) 

    def __setitem__(self, index, value): # Linha(46) para alterar o valor, recebe index e novo valor
        self._data[index] = value # No meu dict determinado index = valor

    def __iter__(self): # Crinado meu iterador(objeto=lista)
        return self

    def __next__(self):
        if self._next_index >= self._index: # Caso o Index do next seja maior que o Index da lista(len)
            self._next_index = 0 # Zera o 'iterator' 
            raise StopIteration # Para a iteração :P

        value = self._data[self._next_index] # Pegando da minha lista o índice 0 (linha14)
        self._next_index += 1 # Aumentando 1 no index para iterar
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    print(lista[0])
    print(vars(lista))
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')