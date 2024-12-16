import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

#  CUIDADO!: fazendo delete sem where
#  SEMPRE QUE EXISTIR DELETE VAI EXISTIR WHERE
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
con.commit()

#  Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
con.commit()

#  Registrar valores nas colunas das tabelas
#  CUIDADO: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)
# cursor.execute(sql, ['Joana', 4])
# cursor.executemany(sql, 
#                    [
#                        ['Joana', 4], ['Lucas', 5]
#                        ]
#                    )
cursor.execute(sql, {'nome': 'Joana', 'peso': 4})
cursor.executemany(sql, [
    {'nome': 'Joana', 'peso': 4},
    {'nome': 'Lucas', 'peso': 5},
    {'nome': 'Maria', 'peso': 7},
    {'nome': 'João', 'peso': 2},
    ])
con.commit()

if __name__ == '__main__':
    print(sql)

    #  SEMPRE QUE EXISTIR DELETE VAI EXISTIR WHERE
    cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = "3"'
    )
    con.commit()

    cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    con.close()