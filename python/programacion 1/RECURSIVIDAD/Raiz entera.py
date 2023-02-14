from Libreria import *

# Modulo Recursivo para calcular la raiz entera
def RaizEntera(n,raiz=0):
    #---- CASO BASE
    if raiz*raiz<=n<(raiz+1)*(raiz+1):
        return raiz
    #---- CASO RECURRENTE
    else:
        return RaizEntera(n,raiz+1)
    
#************+*PROGRAMA PRINCIPAL********
# LEER NUMEROS
n=LeerNroEntero("Ingrese Numero: ",1)
#Mostrar La Raiz entera
print("La raiz entera: ",RaizEntera(n))
