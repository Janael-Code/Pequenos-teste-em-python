import decimal_outra
import base_dec_out

nume_con = str(input("Digite o nume_con a ser convertido :")).upper()
base = int(input("\033[95m]"""" --> Informe a base
< 1 >- Hexadecimal
< 2 >- Octadecimal
< 3 >- Binária
< 4 >- Decimal\n
----> :"""))

baseF = int(input("\033[91m]""""Escolha a base para convesão:
{ 1 }- Hexadecimal
{ 2 }- Octadecimal
{ 3 }- Binária
{ 4 }- Decimal\n 
----> :"""))


if base == 1:
  if baseF == 1:
    print("\033[92m]"  , nume_con)
  
  elif baseF == 2: 
    res = decimal_outra.base_de_outra(nume_con, 16)
    res1 = base_dec_out.bas_decimal_outra(res, 18)
    print("\033[92m]",res1)
  
  elif baseF == 3:
    res = decimal_outra.base_de_outra(nume_con, 16)
    res1 = base_dec_out.bas_decimal_outra(res, 2)
    print("\033[92m]", res1)

  elif baseF == 3:
    res = decimal_outra.base_de_outra(nume_con, 16)
    res1 = base_dec_out.bas_decimal_outra(res, 10)
    print("\033[92m]", res1)

elif base == 2:   
  if baseF == 1:
    res = decimal_outra.base_de_outra(nume_con, 10)
    res1 = base_dec_out.bas_decimal_outra(res, 16)
    print("\033[92m]", res1)
  
  elif baseF == 2:
    res = decimal_outra.base_de_outra(nume_con, 18)
    res1 = base_dec_out.bas_decimal_outra(res, 18)
    print("\033[92m]", res1)
  
  elif baseF == 3:
    res = decimal_outra.base_de_outra(nume_con, 18)
    res1 = base_dec_out.bas_decimal_outra(res, 2)
    print("\033[92m]", res1)

  elif baseF == 3:
    res = decimal_outra.base_de_outra(nume_con, 18)
    res1 = base_dec_out.bas_decimal_outra(res, 10)
    print("\033[92m]", res1)
 

elif base == 3:
  if baseF == 1:
    res = decimal_outra.base_de_outra(nume_con, 2)
    res1 = base_dec_out.bas_decimal_outra(res, 16)
    print("\033[92m]", res1)
  
  elif baseF == 2:
    res = decimal_outra.base_de_outra(nume_con, 2)
    res1 = base_dec_out.bas_decimal_outra(res, 18)
    print("\033[92m]", res1)
  
  elif baseF == 3:
    res = decimal_outra.base_de_outra(nume_con, 2)
    res1 = base_dec_out.bas_decimal_outra(res, 2)
    print("\033[92m]", res1)

  elif baseF == 3:
    res = decimal_outra.base_de_outra(nume_con, 2)
    res1 = base_dec_out.bas_decimal_outra(res, 10)
    print("\033[92m]", res1)


elif base == 4:
  if baseF == 1:
    res = decimal_outra.base_de_outra(nume_con, 10)
    res1 = base_dec_out.bas_decimal_outra(res, 16)
    print("\033[92m]", res1)
  
  elif baseF == 2:
    res = decimal_outra.base_de_outra(nume_con, 10)
    res1 = base_dec_out.bas_decimal_outra(res, 18)
    print("\033[92m]", res1)
  
  elif baseF == 3:
    res = decimal_outra.base_de_outra(nume_con, 10)
    res1 = base_dec_out.base_DecimalPara_Outra(res, 2)
    print("\033[92m]", res1)

  elif baseF == 3:
    res = decimal_outra.base_de_outra(nume_con, 10)
    res1 = base_dec_out.bas_decimal_outra(res, 10)
    print("\033[92m]", res1)