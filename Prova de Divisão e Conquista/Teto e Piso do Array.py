def teto_piso(v,mini,maxi,k):
    if k <= v[mini]:
        return mini

    if k > v[maxi]:
        return -1

    meio = (mini+maxi)//2

    if v[meio] == k:
        return meio

    elif v[meio] < k:
        if meio + 1 <= maxi and k <= v[meio+1]:
            return meio + 1
        else:
            return teto_piso(v,meio+1,maxi,k)
    else:
        if meio - 1 >= mini and k > v[meio-1]:
            return meio
        else:
            return teto_piso(v,mini,meio-1,k)

def teto_piso_aux(v, k):
    mini = 0
    maxi = len(v) -1
    result = teto_piso(v,mini,maxi,k)
    if result ==0:
        return "Teto = "+str(v[result])+" Piso = "+str(-1)
    elif v[result] == k:
        return "Teto = "+str(v[result])+" Piso = "+str(v[result])
    elif result == -1:
        return "Teto = "+str(-1)+" Piso = "+str(v[result])
    else:
        return "Teto = "+str(v[result])+" Piso = "+str(v[result-1])

v = [1, 4, 6, 8, 9]
k = 6
print(teto_piso_aux(v,k))
