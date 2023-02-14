from Libreria import *

# Modulo Recursivo para Invertir un numero
def Invertir(N):
    #---- CASO BASE
    if N<10:
        return N
    #---- CASO RECURRENTE
    else:
        return Invertir(N//10)+ N%10*(10**len(str(N//10)))

#         PROGRAMA PRINCIPAL
# Leer numero
N=LeerNroEntero("Ingrese el número : ",1)
#Mostrar numero invertido
print("Numero invertido : ",Invertir(N))
