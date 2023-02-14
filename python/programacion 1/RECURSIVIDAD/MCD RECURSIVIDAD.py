from Libreria import *

#**********Modulo*****************
def MCD(A,B):
    #-------- CASO BASE
    if A%B==0:
        return B
    #-------- CASO RECURRENTE
    else:
        return MCD(B,A%B)

#**************  Programa principal*****************
# LEER NUMERO
n=int(input("Ingrese un numero = "))
m=int(input("Ingrese un numero = "))

# Mostrar numero de digitos
print("MCD =",MCD(n,m))
