def LeerNota(Texto, Minimo, Maximo = 100000000):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Numero fuera de rango...')
        Nro = int(input(Texto))
    return(Nro)

#CALCULAR LA MENOR NOTA
def Mayor(*Numeros):
    k=1
    for Nro in Numeros:
        if k==1:
            M=Nro
        else:
            M=Nro if M<Nro else M
    return(M)

def Menor(*Numeros):
    k=1
    for Nro in Numeros:
        if k==1:
            M=Nro
        else:
            M=Nro if M<Nro else M
    return(M)
