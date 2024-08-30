# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

data_str_data = '2022-04-20 07:49:23'  # Data salva em string
data_str_fmt = '%Y-%m-%d %H:%M:%S' # Formatando str com legenda da documentação datetime (ano,mes,dia hora,minuto,segundos)
data_str_data1 = '20/04/2022'
data_str_fmt1 = '%d/%m/%Y' # dia mes ano - formatando string(datetime)

# data = datetime(2022, 4, 20, 7, 49, 23)

data = datetime.strptime(data_str_data, data_str_fmt) # Utilizando a função que junta formatação de data, com str data.
data1 = datetime.strptime(data_str_data1, data_str_fmt1) # strptime >
print(f'{data} \n{data1}')