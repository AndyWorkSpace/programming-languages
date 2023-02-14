# ********************** MÓDULOS ***************************
# ----------- Leer Arreglo -------------
def LeerArreglo():
    # -- Leer el número de elementos del arreglo
    N = int(input('Número de elementos del arreglo:'))
    # -- Inicializar un arreglo vacío
    A = []
    # -- Leer los elementos del arreglo
    for K in range(0, N):
        # -- Leer el K-ésimo elemento del arreglo
        print('Ingresar el elemento ',K+1,':',end='')
        Elemento = input()
        A = A + [Elemento]

    # -- Retornar el arreglo
    return N, A

# ----------- Escribir Arreglo -------------
def EscribirArreglo(N, A):
    # -- Escribir los elementos del arreglo
    for K in range(0, N):
        # -- Escribir el K-ésimo elemento del arreglo
        print(A[K])

# ----------- Ubicación de elemento en Arreglo -------------
def UbicacionEnArreglo(Elemento, N, A):
    # -- Ubicar el elemento en el arreglo
    K = 0
    Flag = False
    while (K < N) and (Flag == False):
        Flag = (Elemento == A[K])
        K += 1
    # -- Devolver resultado
    return K-1 if Flag else -1

# ----------- Interseccion -------------
def Interseccion(N1, A1, N2, A2):
    # -- Inicializar el arreglo resultado
    NR = 0
    AR = []
    # -- Ubicar los elementos del primer arreglo en el segundo
    for K in range(0, N1):
        U = UbicacionEnArreglo(A1[K], N2, A2)
        if (U >= 0):
            NR += 1
            AR = AR + [A1[K]]
    # -- Devolver resultado
    return NR, AR

# ----------- Quitar Interseccion -------------
def QuitarInterseccion(N1, A1, NR, AR):
    # -- Ubicar los elementos del primer arreglo en el segundo
    for K in range(0, N1):
        U = UbicacionEnArreglo(A1[K], NR, AR)
        if (U >= 0):
            N1 = N1 - 1
            A1 = A1 - [AR[K]]
    # -- Devolver resultado
    return N1, A1

# ***************** PROGRAMA PRINCIPAL *******************
# -- Leer el arreglo de los integrantes del equipo de Fútbol
print('Ingresar los integrantes del equipo de Fútbo')
NF, AFutbol = LeerArreglo()
print('Ingresar los integrantes del equipo de Basketball')
NB, ABasket = LeerArreglo()

# -- Determinar los integrantes de ambos equipos
NR, AResultado = Interseccion(NF, AFutbol, NB, ABasket)
# -- Mostrar el arreglo resultante
print()
print('Los integrantes de ambos equipos son')
EscribirArreglo(NR, AResultado)

# -- Mostrar equipo de futbol sin los integrantes que se repiten
print()
NF,AF=QuitarInterseccion(NF,AFutbol,NR,AResultado)
print('Equipo de futbol sin integrantes repetidos')
EscribirArreglo(NF,AF)

