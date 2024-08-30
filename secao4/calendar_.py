# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

print(calendar.calendar(2022)) # Exibi calendario do ano no terminar
print(calendar.month(2022, 12)) # Exibi mês de determinado ano
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
# mouthrange exibi o primeiro dia do mês no formato(linha10) e o ultimo dia do mês
print(list(enumerate(calendar.day_name))) # Exemplo de como o formato do primeiro num do dia mês funciona
print(calendar.day_name[numero_primeiro_dia]) # Exibindo o nome do primeiro dia de determinado mês
print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)]) # Exibindo qual nome do ultimo dia do mês
for week in calendar.monthcalendar(2022, 12): # Para cada semana de dezembro 2022
    for day in week: # Para cada dia da semana de dezembro 2022
        if day == 0:
            continue # se o dia for == 0 não faz nada
        print(day)


