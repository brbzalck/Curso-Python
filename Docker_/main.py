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

    #  Começando a manipular dados a partir daqui

    #  Inserindo valor usando um placeholder e um Iterável
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(nome, idade) VALUES (%s, %s) ')
        data = ('Lucas', 24)
        result = cursor.execute(sql, data)
        # print(sql, data)
        # print(result)
    connection.commit()

    #  Inserindo valor usando um placeholder e um Dicionário
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(nome, idade) VALUES (%(name)s, %(age)s) ')
        #   Nome e idade do BD         Nome e Idade do Dicionário
        data2 = {
            "name": "Pedro",
            "age": 22,
        }
        result = cursor.execute(sql, data2)
        # print(sql)
        # print(data2)
        # print(result)
    connection.commit()

    #  Insrindo vários valores usando placeholder e uma Tupla de Dicionários
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(nome, idade) VALUES (%(name)s, %(age)s) ')
        #   Nome e idade do BD         Nome e Idade do Dicionário
        data3 = (
            {"name": "Tiago","age": 22,},
            {"name": "Julia","age": 23,},
            {"name": "Letícia","age": 19,},

            )
        #  Quando usar executemany: colocar dentro de um iterável
        result = cursor.executemany(sql, data3)
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()

    #  Inserindo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(nome, idade) VALUES (%s, %s) ')
        #   Nome e idade do BD         Nome e Idade do Dicionário
        data4 = (
            ("Vanessa", 27),
            ("Esther", 15)
        )
        #  Quando usar executemany: colocar dentro de um iterável
        result = cursor.executemany(sql, data4)
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()

    #  Lendo os dados com SELECT

    with connection.cursor() as cursor:
        menor_id = int(input('Digite o menor id: '))
        maior_id = int(input('Digite o maior id: '))
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
               )
        cursor.execute(sql, (menor_id, maior_id))
        print(cursor.mogrify(sql, (menor_id, maior_id)))

        data5 = cursor.fetchall()
        # for row in cursor.fetchall():
        for row in data5:
            print(row)