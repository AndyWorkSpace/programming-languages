from Libreria import *

#**********Modulo*****************#

# MODULO FIBONACCI
def Figo(N):
    #-------- CASO BASE
    if N<=2:
        return N-1
    #-------- CASO RECURRENTE
    else:
        return Figo(N-1) + Figo(N-2)
    
#**************  Programa principal*****************
# LEER NUMERO
N=LeerNroEntero("ingrese un numero = ",1,10000000)
M=Figo(N)
# Mostrar numero de digitos
print("Fibonaccci de ",N,"es = ",M)
