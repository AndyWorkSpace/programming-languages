# Evaluar funcion

# **********************   Modulos ****************************
# Modulo para leer un numero entero
def LeerNroEntero(Texto, Minimo, Maximo = 100000000):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Numero fuera de rango...')
        Nro = int(input(Texto))
    return Nro


# Modulo para la Funcion
def F(X):
    return X**3 + 2*X**2 - 9*X - 18


# *****************   Programa principal   *******************
# Leer el valor de N
N = LeerNroEntero('Ingrese el valor de N:',1)
# Evaluar la funcion para valores de X = 1, 2, 3, ..., N
NroPositivos = 0
NroNegativos = 0
NroCeros = 0
for X in range(1,N+1):
    Y = F(X)
    if Y < 0:
        NroNegativos += 1
    elif Y == 0:
        NroCeros += 1
    else:
        NroPositivos += 1
# Mostrar resultados
print('Negativos = ',NroNegativos)
print('Iguales a cero = ',NroCeros)
print('Positivos = ',NroPositivos)
