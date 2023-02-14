from Libreria import *

#**********Modulo*****************
def NroDigitosImpar(N):
    #-------- CASO BASE
    if N%2!=0 and N<10:
        return 1
    #-------- CASO RECURRENTE
    else:
        return N%2+ NroDigitosImpar(N//10)
    
#**************  Programa principal*****************
# LEER NUMERO
n=int(input("Ingrese un numero = "))
# Mostrar numero de digitos
print("Número de  digitos impares=",NroDigitosImpar(n))
