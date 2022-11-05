def checa_numero_escondido(numero,numero_oculto):
    full_num = []
    num_oc = []
    final = []
    
    for num in str(numero):
        full_num.append(num)
    
    for num in str(numero_oculto):
        num_oc.append(num)
        
    for num in num_oc:
        if num in full_num:
            final.append(num)
    
    s=[str(i) for i in final]
    x = "".join(s)
    
    if int(x) == numero_oculto:
        z = True
    else:
        z = False
    return z
    
            
    
    


checa_numero_escondido(12345,235)