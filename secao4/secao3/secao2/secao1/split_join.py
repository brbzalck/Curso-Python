"""
split e join com list e str 
strip > para apagar espaços vazio nas laterais da str
split - divide uma string em listas (list) 
join - une uma string 
"""
frase = '   Olha só que   , coisa interessante          ' # Frase zuada com muitos espaços desnecessários
lista_frases_cruas = frase.split(',') # Método usado para separar uma string, (parenteses escolhe aonde vai separar), retornando uma lista

lista_frases = [] # Criando uma lista VAZIA, para armazenar valores da iteração da lista que precisa formatar corretamente
for i, frase in enumerate(lista_frases_cruas): # para cada INDICE de cada ITEM lista_frases_cruas (enumerate para enumerar Indice e Item)
    lista_frases.append(lista_frases_cruas[i].strip()) # Método usado para apagar espaços na esquerda e direita da Str
                      # Depois de usar o método em cada indice, adiciona a lista 

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases) # Método utilizado para unir str(aqui foi lista), atribui uma VAR str que vai definir como vai ser a união
# Ex: VAR = '(aqui defini como vai ser separado)'.join(oque vc vai juntar)
print(frases_unidas)