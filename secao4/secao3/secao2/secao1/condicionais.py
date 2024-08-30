# if / el if     / else
# se / se não se / se não

entrada = input('Você prefere "arroz" ou "feijao"? ') # entrada do tipo de dado do usuário

if entrada == 'arroz':  # se for arroz
    print('Arroz é o melhor carboidrato') # (precisa do tab para pertercer a if)
elif entrada == 'feijao': # se não for arroz mas for feijão
    print('Feijão fresco é uma delícia')# (precisa do tab para pertercer a if)
else: # por fim se nada for True
    print('Acho que você errou o cardápio...') # (precisa do tab para pertercer a if)

