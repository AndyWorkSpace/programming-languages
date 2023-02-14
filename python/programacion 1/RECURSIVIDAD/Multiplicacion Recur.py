# Modulo multiplicacion
def Multiplicacion(a,b):
    # CASO BASE
    if b==0:
        return 0
    # CASO RECURRENTE
    else:
        return a + Multiplicacion(a,b-1)

#           MODULO PRINCIPAL
# LEER NUMEROS
a=int(input("Ingrese un numero = "))
b=int(input("Ingrese un numero = "))

# Mostrar multiplicacion
print(" la multiplicacion = ", Multiplicacion(a,b))

