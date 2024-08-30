# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))


# exemplo de função geradora
def generator(n=0, maximum=10): 
    while True:
        yield n # serve para pausar a função com o atual valor
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=100)
for n in gen:
    print(n)