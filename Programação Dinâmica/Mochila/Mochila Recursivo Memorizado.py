from item import itemMochila
from random import randint
S = dict()

for i in range(0,500):
  S[i] = itemMochila(randint(1,6),randint(10,15))

n = len(S)
w = 100
memoria = [[-1 for i in range(w + 1)] for j in range(n + 1)]

def mochila_recursivo_momorizado(w = 0,S = dict(),n = 0):
  if n == 0 or w == 0:
    return 0
  if memoria[n][w] != -1:
    return memoria[n][w]

  if S[n-1].peso <= w:
    memoria[n][w] = max(S[n-1].valor+mochila_recursivo_momorizado(w-S[n-1].peso,S,n-1),mochila_recursivo_momorizado(w,S,n-1))
    return memoria[n][w]


  elif(S[n-1].peso>w):
    memoria[n][w] = mochila_recursivo_momorizado(w,S,n-1)
    return memoria[n][w]





print(mochila_recursivo_momorizado(w,S,len(S)))