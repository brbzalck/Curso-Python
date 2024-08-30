# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)

from datetime import datetime
from pytz import timezone


data = datetime.now() # Criando a data atual
data_tokyo = datetime.now(timezone('Asia/Tokyo')) # Utilizando timezone para pegar uma região como referência
print('Dia e Hora em Tokyo', data_tokyo) 
print('Dia e Hora no seu local', data)
print()
print('Quantidade de segundos desde 1970:', data.timestamp()) # timestamp(conta os segundos de 01/01/1970 até a data criada)
print(datetime.fromtimestamp(1721673784)) # Cria uma data a partir do timestamp 1/1/70 com a qtd de segundos()