import aula97_n
from aula97_n import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(aula97_n.variavel_modulo) # Pegando a VAR do módulo aula97_n pela linha1
print(variavel_modulo) # Pegando a VAR do módulo aula97_n pela linha2
print(soma(2, 3)) # Usando a função soma do meu módulo aula97_n, pela linha2 do cod
print(aula97_n.soma(2, 3)) # # Usando a função soma do meu módulo aula97_n, pela linha1 do cod

