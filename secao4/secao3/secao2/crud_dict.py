# Manipulando chaves e valores em dicionários
pessoa = {} # Dict vazio

'''
C-REATE CRIAR
R-EAD LER
U-PDATE ATUALIZAR
D-DELETE DELETAR
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

chave = 'nome' # Criando uma chave para o dict

pessoa[chave] = 'Luiz Otávio' # Atribuindo valor para a chave
pessoa['sobrenome'] = 'Miranda' # *** criando uma chave e atribuindo valor *** (create)
print(pessoa)


print(pessoa[chave]) # Acessando um valor (read)

pessoa[chave] = 'Maria' # Atualizando um valor (update)

del pessoa['sobrenome'] # deletando um valor (delete)
print(pessoa) # exibindo meu dict (read)
print(pessoa['nome']) # exibindo chave especifica do meu dict (read)

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None: # método dict GET, utilizado para retornar None, caso 
    print('NÃO EXISTE')# a chave não exista.
else:
    print(pessoa['sobrenome']) # Exibindo chave sobrenome do dict (read)

# print('ISSO Não vai')