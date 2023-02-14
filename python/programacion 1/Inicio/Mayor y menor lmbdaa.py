#CALCULAR LA MENOR NOTA
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
M1=Procesar(lambda M,N : M if M>N else N,18,36,30,24 )
print("Mayor= ",M1)
# Calcular el numero de 6 numeros
M2=Procesar(lambda M,N : M if M<N else N,17,66,32,13,24,82)
print("Menor= ",M2)
