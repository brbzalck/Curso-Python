import calendar
from datetime import date

for week in calendar.monthcalendar(2023, 3): # Para cara semana do mês de 3 de 2023 # noqa 501
    for day in week:  # para cada dia da semana do mes 3 de 2023
        if day == 0:
            continue
        current_day = date(2023, 3, day) # variável que armazena data, e dia do mês # noqa 501
        print(day, current_day.strftime('%A')) # exibi o dia do mês e o nome do dia # noqa 501
