'''
Uma empresa fabrica painéis de LED compostos por quadrados de 1 cm de lado. Nos vértices de cada quadrado fica um LED,
sendo que o tamanho de cada painel é escolhido pelo cliente conforme a sua necessidade. A imagem abaixo mostra um painel de 2 cm por 4 cm, composto por 15 LEDs no total.

Considerando um painel de n por m centímetros, desenvolva um código para calcular o número total de LEDs no painel.

'''
import math
def calcula_total_leds(altura,largura):
    if largura and altura != 0:
        vertices = (altura + 1) * (largura + 1)
    else:
        vertices = 0
    print(vertices)



calcula_total_leds(2, 3)