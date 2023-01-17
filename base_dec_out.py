def bas_decimal_outra(n, base):
  lista = []              

  n = int(n)
  while n > 0:

    nume_ba = n % base
    n = n // base
        
    nume_ba = str(nume_ba)
        
    if nume_ba == "10":
      nume_ba = "A"
    elif nume_ba == "11":
      nume_ba = "B"
    elif nume_ba == "12":
      nume_ba = "C"
    elif nume_ba == "13":
      nume_ba = "D"
    elif nume_ba == "14":
      nume_ba = "E"
    elif nume_ba == "15":
      nume_ba = "F"
        

    lista.append(nume_ba)
  
  lista.reverse() 
  resultado = "".join(lista)
  
  return resultado



