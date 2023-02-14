from Libreria import *

# Modulo Recursivo para Invertir un numero
def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

#            PROGRAMA PRINCIPAL
# Leer numero
cadena=str(input("Ingrese un texto : "))
#Mostrar numero invertido
print("Numero invertido :",invertir_cadena_manual(cadena))
