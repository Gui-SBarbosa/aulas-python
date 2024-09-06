"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_car_pass_radar_1 = velocidade > RADAR_1
car_pass_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
car_mult_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_car_pass_radar_1:
    print('Velocidade do carro passou do radar 1')

if car_pass_radar_1:
    print('carro passou radar 1')

if car_mult_radar_1 and \
        vel_car_pass_radar_1:
    print('carro multado em radar 1')
