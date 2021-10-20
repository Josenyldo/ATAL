def mediana(v1,v2,n):
   #porque o array começa a contar apatir do index 0
  meio= n//2
  print(n,v1,v2)
  if(v1[meio]==v2[meio]):
    return v1[meio]
  elif(meio ==0):
    if(v1[meio] < v2[meio]):
      return (v1[-1]+v2[0])//2
    else:
      return (v1[0]+v2[-1])//2
  else:
    if(v1[meio] < v2[meio]):
      return mediana(v1[meio:],v2[:meio +1],meio)
    else:
      return mediana(v1[:meio+1],v2[meio:],meio)
v2 = [0,1,2,4,5,6]
v1 = [7,9,10,12,13,14]
n = 6
print(mediana(v1,v2,n))