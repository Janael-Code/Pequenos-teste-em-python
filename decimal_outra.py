
def base_de_outra(num, base):
    
    num = str(num)

    base = int(base)

    decimal1 = 0

    lista = []

    for n in num:
        if n == "A":
            n = 10
        elif n == "B":
            n = 11
        elif n == "C":
            n = 12
        elif n == "D":
            n = 13
        elif n == "E":
            n = 14
        elif n == "F":
            n = 15
    
        n = int(n)
        lista.append(n)
    
    leve = len(num)-1

    for a in (lista):
        deci = a * (base) ** (leve)
        leve -=1
        decimal1 += deci
    return decimal1