import sys # modulo usado aqui para contar o tamanho da lista e generator

# FUNÇÃO QUE SABE PAUSAR 

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)] # lista com 1 milhão salvo na memória
generator = (n for n in range(1000000)) # lista com 1 milhão tbm, mas não salvo na memória, pegando um valor por vez(next)

print(sys.getsizeof(lista)) # pegando o tamanho da lista
print(sys.getsizeof(generator)) # pegando o tamanho do generator

print(next(generator)) # pode ser usado com um contador dentro de um for
print(next(generator))



# for n in generator:
#     print(n)
