# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S') # strptime - Tranformando str em Data formatada na VAR data(instância de datetime)
print(data.strftime('%d/%m/%Y')) # strftime - De dentro da minha data formatada, troco a ordem dos valores
print(data.strftime('%d/%m/%Y %H:%M')) 
print(data.strftime('%d/%m/%Y %H:%M:%S')) # Exibindo valores da minha data com strftime()

print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day) # data.year, day, month etc, para pegar valor real da data(em int/float)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)