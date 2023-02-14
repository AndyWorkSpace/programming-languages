# Modulo POTENCIA
def CambiodeBase(n):
    # CASO BASE
    if n<=1:
        return n
    # CASO RECURRENTE
    else:
        return CambiodeBase(n//2)*10+(n%2)

# ----------- MODULO PRINCIPAL -----------
# LEER NUMEROS
a=int(input("Ingrese un numero = "))

# Mostrar multiplicacion
print("Número en base 2 = ", CambiodeBase(a))

