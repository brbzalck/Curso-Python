from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'csv_exemplo.csv'
print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r') as arquivo:
    # leitor = csv.reader(arquivo) # Leitura de arquivo com csv.reader[lista]
    leitor = csv.DictReader(arquivo) # Leitura de arquivo com csv.DictReader

    for linha in leitor:
        print(linha)

