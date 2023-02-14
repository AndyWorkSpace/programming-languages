# ********************** MÓDULOS ***************************
# ----------- Leer Arreglo -------------
def LeerArreglo():
    # -- Leer el número de elementos del arreglo
    N = int(input("Número de elementos del arreglo: "))
    # -- Inicializar un arreglo vacío
    A = []
    # -- Leer los elementos del arreglo
    for K in range(0, N):
        # -- Leer el K-ésimo elemento del arreglo
        Elemento=int(input("Ingresar el elemento:"))
        '''print("Ingresar el elemento ",K+1,":",end="")
        Elemento = input()'''
        A = A + [Elemento]

    # -- Retornar el arreglo
    return N, A
# ----------- Escribir Arreglo -------------
def EscribirArreglo(N, A):
    # -- Escribir los elementos del arreglo
    for K in range(0, N):
        # -- Escribir el K-ésimo elemento del arreglo
        print(A[K])

# ----------- Agregar a Arreglo -------------
def Agregar(N,A,Elem):
    N+=1
    A=A+[Elem]
    return N,A
# ----------- Insertar a Arreglo ------------
def Insertar(N,A,Elem,Pos):
    if (Pos>=0) and (Pos<N):
        N+=1
        A=A+[Elem]
        for k in range(N-1,Pos,-1):
            A[k]=A[k-1]
        A[Pos]=Elem
    return N,A
# ----------- Ubicar en Arreglo ------------
def Ubicacion(N,A,Elem):
    Ubi=-1
    k=0
    while k<N and (Ubi==-1):
        if A[k]==Elem:
            Ubi=k
        else:
            k+=1
    return Ubi
# ----------- Eliminar de Arreglo ------------
def Eliminar(N,A,Pos):
    if (Pos>=0) and (Pos<N):
        N-=1
        for K in range(Pos,N):
            A[K]=A[K+1]
    return N,A[0:N]

# **************** PROGRAMA PRINCIPAL ***************
# -- Leer Arreglo
N,A=LeerArreglo()

# -- Escribir arreglo88
EscribirArreglo(N,A)

# -- agregar en arreglo                               
Elem=int(input("Ingrese el elemento a agregar:"))
N,A=Agregar(N,A,Elem)
print("Elementos:","Arreglo:",A)
print("Elemento agregado:",Elem)

# -- insertar en arreglo
Elem=int(input("Ingrese le elemento a insertar:"))
Pos=int(input("Ingrese la posicion:"))
N,A=Insertar(N,A,Elem,Pos)
print("Elementos:","Arreglo:",A)
print("Elemento insertado:",Elem)

# -- ubicacion en arreglo
Elem=int(input("Ingrese le elemento a buscar:"))
Ubi=Ubicacion(N,A,Elem)
print("Ubicacion de ",Elem,":",Ubi)

# -- eliminar en arreglo
Pos=int(input("Ingrese la posicion a eliminar:"))
N,A=Eliminar(N,A,Pos)
print("Posicion ",Pos," eliminada")
print("Elementos:","Arreglo:",A)

