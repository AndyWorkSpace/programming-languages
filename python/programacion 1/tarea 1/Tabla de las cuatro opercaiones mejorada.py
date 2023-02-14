# Programa de tablas aritmeticas
from Libreria import *
# ************************ MÓDULOS **************************
# Menu de tablas Aritmeticas
def Menu():
    print()
    print(' ***** TABLAS ARITMÉTICAS *****')
    print('1 Sumar')
    print('2 Restar')
    print('3 Multiplicar')
    print('4 Dividir')
    print('5 FIN')
#SUMAR
def Sumar(K,N):
    return(str(K)+'+'+str(N)+'='+str(K+N))
#RESTAR
def Resta(K,N):
    return(str(K+N)+'-'+str(N)+'='+str(K))
#MULTIPLICAR
def Multiplicar(K,N):
    return(str(K)+'x'+str(N)+'='+str(K*N))
#DIVIDIR
def Dividir(K,N):
    return(str(K*N)+'/'+str(N)+'='+str(K))
           
# Tabla Aritmetica 
def TablaAritmetica(titulo,operacion):
    print()
    print('****TABLA ARITMETICA DE '+titulo+'****')
    N=LeerNroEntero('Inregres un numero entre 1 y 12=',1,12)
    for K in range(1,13):
        print(operacion(K,N))

#************ Programa principal************
opcion=0
while opcion !=5:
    #Mostrar menu
    Menu()
    #Leer opcion
    opcion=int(input("ingrese opcion="))
    if opcion==1:
        TablaAritmetica("Sumar",Sumar)
    elif opcion == 2:
        TablaAritmetica("Resta",Resta)
    elif opcion == 3:
        TablaAritmetica("Multiplicar",Multiplicar)
    elif opcion == 4:
        TablaAritmetica("Dividir",Dividir)
    
