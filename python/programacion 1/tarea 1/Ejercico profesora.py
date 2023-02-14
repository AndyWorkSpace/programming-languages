#Modularidad: Mayor y Menor de N Nros
# Mayor de Varios Nros
def Mayor(A,B):
    return A if A>B else B

# menor de Varios Nro
def Menor(A,B):
    return B if B<A else A

def Procesar(Modulo,*Nros):
    A=None
    for Nro in Nros:
        if A==None:
            A=Nro
        else:
            A=Modulo(A,Nro)
    return(A)

# Programa Principal
# Calcular el Mayor de 4 Nros.
M1=Procesar(Mayor,18,36,30,24)
print("Mayor = ",M1)
# Calcular el menor de 6 Nros.
M2 =Procesar(Menor,17,66,32,13,24,82)
print("Menor = ",M2)
