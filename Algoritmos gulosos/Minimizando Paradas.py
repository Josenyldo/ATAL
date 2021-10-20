def minimizandoParada(chegada,tanque,postos,quantParadas):
    contador = 0
    posicao = 0
    abastecimento =  tanque
    postos.append(chegada)
    for i in range(quantParadas):
        tanque = (tanque - (postos[i] - posicao))
        posicao =  posicao = postos[i]
        if  postos[i + 1] - posicao > tanque:
            tanque = abastecimento
            if(postos[i + 1] - posicao > tanque):
                return -1
            contador += 1

    return  contador


D = 950
tanque = 400
paradas = 4
postos = [200,375,550,750]

print(minimizandoParada(D,tanque,postos,paradas))

D = 10
tanque = 3
paradas = 4
postos = [1,2,5,9]

print(minimizandoParada(D,tanque,postos,paradas))