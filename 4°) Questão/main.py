from funcoes import ordena, juntar_lista
from random import randint

lista1 = []
lista2 = []
for add in range(10):
    lista1.append(randint(0, 50))
    lista2.append(randint(0, 50))

print(f"Lista 1: ", end = "")
for n in lista1:
  print(f"{n}", end=", ")

print(f"\nLista 2: ", end = "")
for n in lista2:
  print(f"{n}", end=", ")


lista3 = juntar_lista(lista1,lista2)
print(f"\n\nLista ordenada (lista 3): ", end = "")
for n in lista3:
  print(f"{n}", end=", ")

