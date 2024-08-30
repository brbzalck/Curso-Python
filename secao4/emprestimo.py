# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime 
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20) # Criando uma data simples com datetime(ano, mes, dia)
cinco_anos = relativedelta(years=5) # relativedelta para armazenar 5 anos numa VAR
data_final = data_emprestimo + cinco_anos
print(data_final)


# Criando parcelas da data inicial até a data final
data_parcelas = [] # armazena parcelas
data_parcela = data_emprestimo # Pegando uma data incial como referencia
while data_parcela < data_final: 
    data_parcelas.append(data_parcela) # adiciona data na lista
    data_parcela += relativedelta(months=+1) # sobe um mês na data

numero_parcelas = len(data_parcelas) # Contem qnt de parcelas(meses60)
valor_parcelas = valor_total / numero_parcelas # Dividindo valor total pelos meses de pagamento

for data in data_parcelas: # Exibindo cada parcela formatada bunitinha
    print(data.strftime('%d/%m/%Y'), f'R${valor_parcelas:,.2f}') # formatação float , . 00
    # Usando a função strftime na nossa data, para exibir no nosso formato br dia/mes/ano

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar'
    f' em {cinco_anos.years} anos'
    f' ({numero_parcelas} meses) em parcelas de'
    f'R$ {valor_parcelas:,.2f}.'
)