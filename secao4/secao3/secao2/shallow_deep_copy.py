# Métodos úteis dos dicionários em Python
# copy - retorna uma cópia rasa (shallow copy)
# copy == cópia raza(se existir dados mutáveis dentro de uma cópia, vai alterar as duas estruturas)

# módulo utilizado para fazer uma cópia profundo(definitivamente separo uma copia da outra)
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# d2 = d1.copy() # Cópia raza, dados mutáveis vão ser alterados nos dois lugares

d2 = copy.deepcopy(d1) # Módulo utilizado p/ de fato separar uma cópia da outra
#                       mesmo com dados mutáveis dentro do dict
d2['c1'] = 1000 
d2['l1'][1] = 999999

print(d1)
print(d2)