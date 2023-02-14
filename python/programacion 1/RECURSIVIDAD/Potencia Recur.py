# Modulo POTENCIA
def Potencia(a,n):
    # CASO BASE
    if n==0:
        return 1
    # CASO RECURRENTE
    else:
        return a*Potencia(a,n-1)

# ----------- MODULO PRINCIPAL -----------
# LEER NUMEROS
a=int(input("Ingrese un numero = "))
n=int(input("Ingrese la potencia = "))

# Mostrar multiplicacion
print(" la potencia = ", Potencia(a,n))

