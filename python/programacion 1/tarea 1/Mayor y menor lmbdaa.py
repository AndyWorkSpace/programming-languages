#CALCULAR LA Nota
def Procesar(Modulo,*Nros):
    A=None
    for Nro in Nros:
        if A==None:
            A=Nro
        else:
            A=Modulo(A,Nro)
    return(A)

# PROGRAMA PRINCIPAL
# Calcular el numero de 4 numeros
M=Procesar(lambda M,N : M if M>N else N,18,36,30,24 )
print("Número Mayor = ",M)
# Calcular el numero de 6 numeros
N=Procesar(lambda M,N : M if M<N else N,17,66,32,13,24,82)
print("Número Menor = ",N)
