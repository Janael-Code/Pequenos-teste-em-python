with open("ListaDeSeries.txt", "r") as lista:
  ler = lista.readlines()
  for series in ler:
    print(series.replace("\n", ""))