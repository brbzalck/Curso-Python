# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql

connection = pymysql.connect(
    host='localhost',
    #  Especificando a porta que joga p dentro do container
    port=3307,
    user='usuario',
    password='senha',
    database='base_de_dados',
)

#  Usando context manager par fechar automaticamente a conexão:
with connection:
     with connection.cursor() as cursor:
          print(cursor)
          