def frequecia_elementos(v,mini,maxi,freq):
    if mini > maxi:
        return
    if v[mini] == v[maxi]:
        quantidade = freq.get(v[mini])
        if quantidade is None:
            quantidade = 0
        freq[v[mini]] = quantidade + (maxi - mini+1)
        return
    meio = (mini+maxi)//2
    frequecia_elementos(v,mini,meio,freq)
    frequecia_elementos(v,meio+1,maxi,freq)

def frequecia_elementos_aux(v):
    mini = 0
    maxi = len(v) -1
    freq = {}
    frequecia_elementos(v,mini,maxi,freq)
    for i in freq.keys():
        print(freq[i]," ocorre ",i," vezes ")


v = [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]

print(frequecia_elementos_aux(v))


