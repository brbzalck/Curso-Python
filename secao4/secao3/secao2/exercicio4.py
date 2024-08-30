"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9], #####
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def lista_autentica(lista): # Definindo uma função que recebe lista
    if lista == list(set(lista)): # se a lista depois de passar pelo set() ainda for ela mesma == autentica
        return print(f'A lista {lista} é autentica.') # return para sair da função com o valor desejado e não executar mais nada
#                                                      partindo para próx lista das listas

    lista_vazia = [] # criando uma lista vazia para fazer verificações

    for item in lista: # para cada item da minha lista
        verifica = item in lista_vazia # Criando uma VAR verificadora, se não estiver vai adicionando a lista
        if verifica: # caso a VAR for True
            return print(f'O primeiro número duplicado da lista {lista} é {item}') # return saindo da minha função com o resultado desejado
        else: # caso VAR verifica for False
            lista_vazia.append(item) # adiciona o item a lista vazia   

for lista in lista_de_listas_de_inteiros: # para cada lista das minhas listas
    lista_autentica(lista) # executa a função lista

'''_____________________________________________________________________________________________________________________________________'''

def duplicado(lista): # Definindo a função duplicado(lista)
    s1 = [] # Criando uma lista vazia para verificação
    for i in lista: # para cada item da lista recebida como parâmetro
        if i in s1: # verifica se i está na lista vazia
            return i # se sim a função nessa lista retorna i = valor repetido primeiramente
        s1.append(i) # se não, adiciona a lista vazia
    return -1 # caso todos os i sejam autênticos, a função nessa lista retorna -1

for i in lista_de_listas_de_inteiros: # para cada lista dentro da lista de listas
    print(i, duplicado(i)) # exibi, primeiro a lista<<< e depois a função(lista da vez)
'''_____________________________________________________________________________________________________________________________________'''

def encontra_primeiro_duplicado(lista_de_inteiros): # definindo função que recebe lista_de_inteiros
    numeros_checados = set() # criando um conjunto set para verificação
    primeiro_duplicado = -1 # criando uma flag, caso não tenha número duplicado

    for numero in lista_de_inteiros: # para cada numero em lista_de_inteiros(lista recebida como parâmetro(linha74))
        if numero in numeros_checados: # se o numero estiver em numeros_chegar(set de verificação)
            primeiro_duplicado = numero # salva o primeiro duplicado 
            break # encerra o for

        numeros_checados.add(numero) # caso não esteja nos num checados(linha65) cai aqui e adiciona no set de verificação

    return primeiro_duplicado # faz a função retornar o primeiro duplicado(caso linha66 == True) ou então usa flag (linha62)


for lista in lista_de_listas_de_inteiros: # para cada lista da lista de listas
    print(lista, encontra_primeiro_duplicado(lista)) # Exibi a lista e executa a função(com o argumento da lista da vez)