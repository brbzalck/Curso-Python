# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
'''________________________________________________________________________________________________________________________________________________'''

# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys

platform = 'A MINHA' # importando um módulo normalmente
print(sys.platform)
print(platform)
'''_______________________________________________________________________________________________________________________________________________'''

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo***
from sys import exit, platform # importando alguns métodos do módulo
 
print(platform)
'''_______________________________________________________________________________________________________________________________________________'''

# alias 1 - import nome_modulo as apelido
import sys as s # Renomeando módulos

sys = 'alguma coisa'
print(s.platform)
print(sys)
'''________________________________________________________________________________________________________________________________________________'''

# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex # importando método do módulo e renomeando-o
from sys import platform as pf

print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem
'''________________________________________________________________________________________________________________________________________________'''
# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import exit, platform

print(platform)
exit()