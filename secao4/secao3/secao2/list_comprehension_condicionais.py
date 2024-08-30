numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x] # jogando 2 for numa mesma VAR em tempo de execução
print(numeros)
print(flat) # em suma, jogando tudo para uma única lista


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novo_numeros = [numero for numero in numeros if numero > 5] # Condicinal no final da LC (if depois do for)
impares = [numero for numero in numeros if numero % 2 != 0] # Condicinal no final da LC
pares = [numero for numero in numeros if numero % 2 == 0] 
outro_if = [
    numero
    if numero != 6 else 600 # Ternária logo no começo da LC(if antes do for)
    for numero in pares
]

print(numeros)
print(novo_numeros)
print(impares)
print(pares)
print(outro_if)