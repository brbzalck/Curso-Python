# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S' # Salvando a formatação em uma variável
data_inicio = datetime.strptime('08/05/2000 09:30:30', fmt) # Formatando a data em str com srtptime, VAR=fmt(formatação)
data_fim = datetime.strptime('22/07/2024 08:20:20', fmt) 
delta = timedelta(days=10, hours=2) # Classe que adiciona/subtrai dias horas e segundos
print(data_fim - delta) # Tirando 10dias e 2hs da data_fim ;p
print()

delta_relative = relativedelta(data_fim, data_inicio) # relativedelta(compara duas datas)
print(delta_relative.days, delta_relative.years) # Diferença de dias e anos entre as datas
print(data_fim)
print(data_fim + relativedelta(seconds=60, minutes=10))
print()
''''__________________________________________________________'''
print()
delta1 = data_fim - data_inicio # Raiz - Calculando duas datas(Instâncias de Datetime)
print(delta1) # Quantos dias de vida eu tenho
print(delta1.days, delta1.seconds, delta1.microseconds) # Dias segundos e microsegundos
print(delta1.total_seconds()) # Todos os meus segundos de vida até agora(aproximadamente)
print(data_fim > data_inicio) 
print(data_fim == data_inicio)