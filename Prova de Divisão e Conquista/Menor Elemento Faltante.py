def menorElemento(v1, min=0, max=None, ):
    if max == None:
        max = len(v1) - 1
    if (min > max):
        return min
    meio = min + (min - max) // 2
    if (v1[meio] == meio):
        return menorElemento(v1, meio + 1, max)
    else:
        return menorElemento(v1, min, meio + 1)

v2 = [3,1,2,3,4,5,6]
print(menorElemento(v2))