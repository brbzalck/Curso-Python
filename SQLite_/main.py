import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

#  CUIDADO!: fazendo delete sem where
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
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "Lucas Barbosa", 9.9), (NULL, "João Vitor", 16)'
)
con.commit()



cursor.close()
con.close()
