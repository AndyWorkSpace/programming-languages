# Programa 
# Programa para calcular la mayor distancia de N puntos al origen

# Modulo para leer un numero entero
def LeerNroEntero(Texto, Minimo, Maximo = 100000000):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Numero fuera de rango...')
        Nro = int(input(Texto))
    return Nro
# Módulo para leer un punto
def LeerPunto():
    #print(Texto)
    X = float(input('Ingrese el valor de la coordenada X: '))
    Y = float(input('Ingrese el valor de la coordenada Y: '))
    return X, Y

# Módulo para calcular la distancia entre dos puntos
def Distancia(X1, Y1, X2, Y2):
    return ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5


# Módulo para determinar el mayor de dos números
def MayorDos(A, B):
    return A if A > B else B
# Programa Principal
# Leer el numero de puntos
N = LeerNroEntero('Ingresar el numero de puntos:', 1)

# Leer los puntos y determinar la distancia mayor
DistanciaMayor = 0;
for K in range(1, N+1):
    # Leer el K-esimo punto
    X, Y = LeerPunto()
    # Calcular la distancia al origen
    distancia = Distancia(X, Y, 0.0, 0.0)
    # Verificar si es la mayor distancia
    DistanciaMayor = MayorDos(DistanciaMayor, distancia)
        
# Mostrar resultado
print('La mayor distancia es:', DistanciaMayor)
    
