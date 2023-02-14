from Libreria import *

#**********Modulo*****************
def NroDigitos(N):
    #-------- CASO BASE
    if N<10:
        return 1
    #-------- CASO RECURRENTE
    else:
        return 1+ NroDigitos(N//10)
    
#**************  Programa principal*****************
# LEER NUMERO
n=int(input("Ingrese un numero = "))

# Mostrar numero de digitos
print("Número de  digitos =",NroDigitos(n))
