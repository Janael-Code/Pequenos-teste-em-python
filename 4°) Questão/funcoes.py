def ordena(numeros):
  for posi in range(len(numeros)):
    numeroAtual = numeros[posi]

    while posi > 0 and numeros[posi-1] > numeroAtual:
      numeros[posi] = numeros[posi-1]
      posi -= 1

    numeros[posi] = numeroAtual
  return numeros 

def juntar_lista(lista1,lista2):
  lista3 = ordena(lista1 + lista2)
  return lista3


