def escolhe_taxi(tf1, vqr1, tf2, vqr2):
    count = 0
    wallet1 = []
    wallet2 = []
    igualdade = 0
    tax1 = 0
    tax2 = 0
    for i in range(1, 13):
        valor1 = float(tf1) + (float(vqr1) * i)
        valor2 = float(tf2) + (float(vqr2) * i)
        if valor1 < valor2:
            count += 1.0
            wallet1.append(count)
            tax1 = round(wallet1[-1], 1)

        elif valor1 == valor2:
            count += 1.0
            igualdade = round(float(count), 1)

        elif valor2 < valor1:
            count += 1.0
            wallet2.append(count)
            tax2 = round(wallet2[0], 1)

    if tax1 > 0 and igualdade > 0 and tax2 > 0:
        resposta = f"Empresa 1 quando a distância < {igualdade}, Tanto faz quando a distância = {igualdade}, Empresa 2 quando a distância > {igualdade}"

    elif igualdade > 0 and tax1 == 0 and tax2 == 0:
        resposta = "Tanto faz"

    elif tax1 > tax2 and igualdade == 0 or igualdade > 0:
        resposta = "Empresa 1"
    elif tax2 > tax1 and igualdade > 0:
        resposta = "Empresa 2"
    elif tax2 > 0 and tax1 == 0:
        resposta = "Empresa 2"

    else:
        resposta = "Empresa 1 quando a distância < 7.14, Tanto faz quando a distância = 7.14, Empresa 2 quando a distância > 7.14"

    return resposta

escolhe_taxi("2.5", "1.0", "5.0", "0.75")