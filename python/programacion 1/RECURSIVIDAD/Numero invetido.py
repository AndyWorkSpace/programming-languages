from Libreria import *

# MODULO INVERTIR NUMERO
def Invertir(n,NroInvertido=0):
    #---- CASO BASE
    if n==0:
        return NroInvertido
    #---- CASO RECURRENTE
    else:
        return Invertir(n//10,NroInvertido*10+n%10)

#****** PROGRAMA PRINCIPAL*********
# LEER NUMERO
n=LeerNroEntero("Ingrese Numero: ",1)
#MOSTRAR NUMERO INVERTIDO
print("Numero invertido: ",Invertir(n))
