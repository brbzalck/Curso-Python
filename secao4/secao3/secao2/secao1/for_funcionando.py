"""
COMO FUNCIONA O FOR COMO FUNCIONA O FOR COMO FUNCIONA O FOR
Iterável -> str, range, etc (__iter__) 
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""


# for letra in texto
texto = 'Luiz'  # iterável

iteratador = iter(texto)  # iterator -> Var que retorna o Iterador da Iteração

while True: # Enquato
    try: # Tenta executar
        letra = next(iteratador) # Começando do item 0, puxa os próximos Valores
        print(letra) # Exibe na tela a letra que foi iterada
    except StopIteration: # Quando der erro pelo fato de não ter mais oque Iterar, "except StopIteration" para terminar e o codigo nao quebrar
        break # termina

for letra in texto:
    print(letra)