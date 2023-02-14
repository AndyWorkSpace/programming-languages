#----Leer arreglo
def LeerArreglo():
    #-- Leer el numero de elementos del arrelo
    N=int(input("Numero de elementos del arreglo: "))
    #-- Inicializar un arreglo
    A=[]
    #.. Leer los elemenros del arreglo
    for k in range(0,N):
        #-- Leer el k-enesimo elemetno del rrelo
        print('Ingresar el elemento',k,':',end='')
        Elemento = float(input())
        A=A+[Elemento]
    #-- Retornar le arreglo
    return N,A
        
# Escrivbir arreglo
def EscribirArreglo(N,A):
    #-- Escribir los elementos del arreglo
    for k in range(0,N):
        #-- Escribir el k-enesimo elemento del arreglo
        print(A[k])
'''
def EscribirArreglo(N,A):
    for k in A:
        print(k)'''

#*************** Programa principal *********#
#--Leer Arreglo
N,A=LeerArreglo()
#-- Mostrar el arreglo
print()
print("Los elementos del arreglo son")
EscribirArreglo(N,A)
