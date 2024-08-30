from secao1 import modulo # importando apenas o modulo para secao2(modulo.algumacoisa)
import secao1.modulo # Importando modulo da secao1 para secao2(secao1.modulo.algumacoisa)
from secao1.modulo import * # Má pratica

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(secao1.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)

### O DIRETÓRIO DE ONDE ESTÁ O MODULO TEM QUE ESTAR VISÍVEL PARA O MÓDULO MAIN(ELE SO EXERGA MODULOS/PASTAS IRMÃOS E FILHOS)