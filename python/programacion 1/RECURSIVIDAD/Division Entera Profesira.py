from Libreria import *

# Modulo Recursivo para calcular la division entera
def DivisionEntera(N,M):
    #----- CASO BASE
    if N<M:
        return 0
    #----- CASO RECURRENTE
    else:
        return 1+DivisionEntera(N-M,M)

#************+*PROGRAMA PRINCIPAL********
# LEER NUMEROS
N=LeerNroEntero("Ingrese Dividendo : ",1)
M=LeerNroEntero("Ingrese Divisor : ",1)
#Mostrar divison entera
print("La divion entera es: ",DivisionEntera(N,M))
