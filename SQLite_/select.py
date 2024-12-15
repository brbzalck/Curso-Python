import sqlite3
from main import DB_FILE, TABLE_NAME

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

#  Pegando o ID 3 da tabela em específico
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
    )
row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

print()

#  Pegando todos os dados da tabela
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    )

for row in cursor.fetchall():
    #  Desempacotando a tupla row por índice específico
    # _id = row[0]
    # name = row[1]
    # weight = row[2]

    #  Desempacotando a tupla row diretamente
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
con.close()
