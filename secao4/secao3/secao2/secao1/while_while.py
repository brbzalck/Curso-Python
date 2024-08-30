"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1 
while linha <= qtd_linhas: # Esse while so vai executar denovo quando o while de baixo acabar
    coluna = 1             
    while coluna <= qtd_colunas: # Depois de rodar 5 vezes ele volta p while de cima
        print(f'{linha = } {coluna = }') # linha mantém 1 pq não saiu desse while ainda
        coluna += 1 # coluna vai crescer até a expressão L14 quebrar
    linha += 1 # depois que sair do while de cima, passa a ser linha 2


print('Acabou')