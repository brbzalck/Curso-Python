"""
Repetições
while (enquanto) Vai funcionar enquanto a VAR for verdadeira
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao: # parecido com If, se a condição for verdadeira, então while começa
    nome = input('Qual o seu nome: ') 
    print(f'Seu nome é {nome}') 

    if nome == 'sair': # A partir daqui, se o usuário não digitar 'sair', while recomeça
        break # Termina com o laço de repetição while

print('Acabou')