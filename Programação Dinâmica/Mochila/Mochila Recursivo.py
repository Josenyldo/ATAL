from item import itemMochila
from random import randint

S = dict()
for i in range(0,80):
  S[i] = itemMochila(randint(1,6),randint(10,15))
w = 100
n = len(S)
def mochila_recursivo(w, S, n):

  if n== 0 or w ==0:
    return 0
  if S[n-1].peso <= w:
    return max(S[n-1].valor + mochila_recursivo(w - S[n - 1].peso, S, n - 1), mochila_recursivo(w, S, n - 1))
  else:
    return mochila_recursivo(w, S, n - 1)




print(mochila_recursivo(w, S, n))
