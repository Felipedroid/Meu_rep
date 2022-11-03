
import math
def calcula_porcentagem_sorteio(assinante,minutos_assistidos):
    count = 0
    dic_specs = {}
    probabilidade = []
    
    
    
    for i in assinante:
        if assinante[count] == False:						#Adciona cada item ao dicionário com os minutos ja convertidos em horas.
            dic_specs[count] = math.ceil(minutos_assistidos[count] / 60)
            count += 1								#Verifica se o assinante é premium ou nao
        else:
            dic_specs[count] = 2*(math.ceil(minutos_assistidos[count] / 60))        
            count += 1								 
    
    soma_horas = math.ceil(sum(dic_specs.values()))				 #soma todas os values do dicionário e arredonda para cima

    for i in dic_specs:        
        probabilidade.append(int(round(dic_specs[i]/soma_horas*100)))		 #Realiza o calculo da probabilidade de cada Value

    print(probabilidade)

calcula_porcentagem_sorteio([True,False],[60,120])

