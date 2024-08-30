"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis) 
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # se eu quiser atribuir uma lista para uma variável e editar = copy
# nao devo atribuir uma lista a outra lista, vai apontar para o mesmo lugar na memória e editar a mesma coisa
lista_a[0] = 'Qualquer coisa' # editando a lista_a especifica, porque está separada da b
print(lista_a) # lista original
print(lista_b) # cópia da lista_a (independente da mesma)

# Ex lista_b = lista_a == mesma coisa, oque eu mexer em uma muda na outra também