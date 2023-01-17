def num():
  listaNumeros = []
  numeros_fatorados = []
  tamanho = int(input("Tamanho da lista: "))
  for i in range (tamanho):
    listaNumeros.append(int(input("Digite um número: ")))

  for n in listaNumeros:
    numeros_fatorados.append(calcularFatorial(n))

  return numeros_fatorados, listaNumeros

def calcularFatorial(num): 
  count = num
  fatorial = 1
  while count > 0:
    fatorial *= count
    count -= 1
  return fatorial