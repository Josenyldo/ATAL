from operator import itemgetter
def quantPlataforma(partida,chegada):
    horarios = dict()
    cont = 1
    for  i in range(len(chagada)):
        horarios[chegada[i]] = partida[i]

    horarios = sorted(horarios.items(),key=itemgetter(0))

    for i in range(len(horarios) -1):
        chegada_individual = horarios[i +1][0]
        partida_individual = horarios[i][1]
        if partida_individual > chegada_individual:
            cont+=1
        return cont
chagada = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
partida = [2.30, 3.40,3.20, 4.30, 4.00, 5.20]

print(quantPlataforma(partida,chagada))