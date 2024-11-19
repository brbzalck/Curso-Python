primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O valor {primeiro_valor} é maior que o valor {segundo_valor}.')
elif segundo_valor > primeiro_valor:
    print(f'O valor {segundo_valor} é maior que o valor {primeiro_valor}. ')
else:  
    print('O valor digitado é igual.')