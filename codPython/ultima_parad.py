
#Você e seu time estão desenvolvendo um sistema de indicações de postos de gasolina que ficam próximos da localização atual do veículo. N
#No modo de direção “viagem”, a funcionalidade a ser desenvolvida é de indicar ao condutor o posto mais distante possível dentro do limite atual de combustível.
#E caso não exista posto de gasolina, retornar -1
#você terá as seguintes informações: consumo médio de combustível, quantidade de combustível restante no veículo e um array contendo distâncias dos postos de gasolinas.
#Exemplo:
#Combustivel (em litros): 2
#Consumo médio (km/l): 8
#Postos de Gasolina (km): [2, 15, 22, 10.2]
combustivel = 0
consumo  = 0
postos_de_gasolina = []
distancia = 0
def ultima_parada(combustivel,consumo,postos_de_gasolina):
    postos_de_gasolina.sort(reverse=True)
    distancia = combustivel * consumo
    for item in postos_de_gasolina:
        if item <= distancia:
            parada = item
            break
        else:
            parada = -1
    return parada


ultima_parada(2,8,[2,15,22,11]) #deve retornar 15