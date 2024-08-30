"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60  # velocidade atual do carro
local_carro = 102  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_radar = velocidade > RADAR_1
range_carro = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
# Criei uma variavel para definir uma distância do km 99 ao 101 conforme o exercicio (Range do radar - 3km)

if velocidade_radar: # If para mostrar velocidade excedida ou n
    print('Velocidade excedida')
else:
    print('O carro estava em velocidade permitida.')

if range_carro and velocidade_radar: # IF com Range do radar & carro está em velocidade excedida ou não,
    print(f'Carro foi multado no Km {LOCAL_1}') # Carro multado se o range e velocidade > for True
else:
    print('Carro não foi multado')  