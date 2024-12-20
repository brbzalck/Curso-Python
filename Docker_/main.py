# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql
import dotenv
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    #  Especificando a porta que joga p dentro do container
    port=int(os.environ['MYSQL_PORT']),
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

#  Usando context manager par fechar automaticamente a conexão:
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        #  esse comando limpa a tabela CUIDADO para usar em ambiente de produção
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(nome, idade) VALUES (%s, %s) ')
        data = ('Lucas', 24)
        result = cursor.execute(sql, data)
        print(sql, data)
        print(result)
    connection.commit()