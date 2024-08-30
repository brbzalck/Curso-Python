#INIT SERVE PARA EU IMPORTAR DETERMINADOS MÓDULOS, A FIM DE DEIXAREM DISPONÍVEIS NA PASTA ONDE O INIT SE ENCONTRA
# EX: import secao1.(aqui fica tudo que estiver importado no init)

# print('Você importou a seção 1')

# def dobra(n):
#     return n * 2

from secao1.modulo import * # Único caso, aonde usar import * é necessário
from secao1.round import *