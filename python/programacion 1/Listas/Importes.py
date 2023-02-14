#----Leer arreglo
def LeerArreglo():
    #-- Leer el numero de elementos del arrelo
    N=int(input("Numero de elementos del arreglo: "))
    #-- Inicializar un arreglo
    A=[]
    #.. Leer los elemenros del arreglo
    for k in range(0,N):
        #-- Leer el k-enesimo elemetno del rrelo
        print('Ingresar el importe',k,':',end='')
        Elemento = float(input())
        A=A+[Elemento]
    #-- Retornar le arreglo
    return N,A

# Modulo determinar mayor importe
def DeterminarMayor(N,A):
    # asumir el primer elemento mayor
    mayor=A[0]
    for i in range(1,N):
        if mayor<=A[i]:
            mayor=A[i]
    return mayor

# Modulo determinar menor importe
def DeterminarMenor(N,A):
    menor=A[0]
    for i in range(1,N):
        if menor>=A[i]:
            menor=A[i]
    return menor

# Modulo calcular Promedio
def Promedio(N,A):
    suma=0
    for i in range(0,N):
        suma=suma+A[i]
    promedio=suma/N
    return promedio

'''
def EscribirArreglo(N,A):
    for k in A:
        print(k)'''

#*************** Programa principal *********#
#--Leer Arreglo
N,A=LeerArreglo()
#-- Mostrar el arreglo
print("Lista:",A)
# Mostrar mayor importe
print("El mayor importe es: ",DeterminarMayor(N,A))
# Mostrar menor importe
print("El menor importe es: ",DeterminarMenor(N,A))
# Mostrar Promedio
print("El Promedio es: ",Promedio(N,A))
