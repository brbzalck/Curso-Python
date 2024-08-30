lista = []
for x in range(3):
    for y in range(3): # fazendo uma tupla normal com  2 for 00 01 02 10 11 12
        lista.append((x, y))


lista = [(x, y) for x in range(3) for y in range(3)]
# Fazendo em uma list comprehension o mesmo algoritmo acima

# lista = [
#     [(x, letra) for letra in 'Luiz'] # exemplo de list comprehesion dentro do valor da list comprehesion em si
#     for x in range(3)
# ]

print(lista)