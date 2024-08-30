import importlib # Módulo usado para recarregar um módulo

import aula98_m # pois sempre que importar um módulo, será feito apenas uma vez

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m) # importlib.reload(vai recarregar o módulo novamente)
    print(i)

print('Fim')