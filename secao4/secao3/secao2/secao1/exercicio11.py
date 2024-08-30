"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os # Usada para limpar o terminal por enquanto

lista = [] # Criando a lista fora do while p não resetar ela smp que while rodar dnv

while True:

    oque_fazer = input('Selecione uma opção: \n [i]nserir [a]pagar [l]istar: ')
    entradas_permitidas = 'ial' # selecionando as entradas permitidas

    if oque_fazer not in entradas_permitidas: # se a entrada não for permitida
        print('Por favor, selecione uma das opções corretamente. ') # exibe erro 1
        continue # volta ao começo do while

    elif oque_fazer == 'i': # Caso entrada seja i
        os.system('cls') # limpa o terminal toda vez que for adicionar algum item

        novo_item = input('Novo item: ') # atribuindo o novo item para a VAR
        lista.append(novo_item) # adicionando um novo item a lista
    
    elif oque_fazer == 'l': # Caso a entrada seja l
        os.system('cls') # limpa o terminal toda vez que for listar a lista
        if len(lista) == 0: # se a lista estiver vazia
            print('Nada para mostrar.')
        for indice, nome in enumerate(lista): # função específica do python para enumerar colocando o índice e nome da lista(enumerate.py caso duvidas)
            print(indice, nome) # enumerando minha lista, e já colocando em duas VAR para exibir fora do tuple

    elif oque_fazer == 'a': # Caso a entrada seja a

        entrada_a_str = input('Qual índice do ítem deseja apagar: ')
        
        try: # Tenta executar
            apagar = int(entrada_a_str) # tranformando a entrada em INT
            lista.pop(apagar) # Apagando item da lista conforme o índice da entrada
        except ValueError: # CASO DER O ERRO ValueError, VAI EXIBIR O PRINT NA TELA E O CÓDIGO NÃO VAI QUEBRAR VOLTANDO AO WHILE NOVAMENTE
            print('Digite um número inteiro') # Número não é inteiro
        except IndexError: # CASO DER O ERRO IndexError, VAI EXIBIR O PRINT NA TELA E O CÓDIGO NÃO VAI QUEBRAR
            print('Índice não existe na lista') # Índice inexistete
        except Exception: # Usado para quando o erro é desconhecido
            print('Erro desconhecido')