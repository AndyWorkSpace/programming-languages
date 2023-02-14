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
# Tabla Aritmetica de Sumar
def Sumar():
    print()
    print('***** TABLA ARITMÉTICA DE SUMAR *****')
    N = LeerNroEntero('Ingrese un número entre 1 y 12:',1,12)
    for K in range(1,13):
        print(str(K)+'+'+str(N)+'='+str(K+N))
# Tabla Aritmetica de Restar
def Restar():
    print()
    print('***** TABLA ARITMÉTICA DE RESTAR *****')
    N = LeerNroEntero('Ingrese un número entre 1 y 12:',1,12)
    for K in range(1,13):
        print(str(K+N)+'-'+str(N)+'='+str(K))
# Tabla Aritmetica de Multiplicar
def Multiplicar():
    print()
    print('***** TABLA ARITMÉTICA DE MULTIPLICAR *****')
    N = LeerNroEntero('Ingrese un número entre 1 y 12:',1,12)
    for K in range(1,13):
        print(str(K)+'x'+str(N)+'='+str(K*N))
# Tabla Aritmetica de Dividir
def Dividir():
    print()
    print('***** TABLA ARITMÉTICA DE DIVIDIR*****')
    N = LeerNroEntero('Ingrese un número entre 1 y 12:',1,12)
    for K in range(1,13):
        print(str(K*N)+'/'+str(N)+'='+str(K))

# ******************* PROGRAMA PRINCIPAL **************************
Opcion = 0;
while Opcion != 5:
    # Mostrar Menu
    Menu()
    # Leer Opción
    Opcion = int(input('Ingrese opción -->'))
    if Opcion == 1:
        Sumar()
    elif Opcion == 2:
        Restar()
    elif Opcion == 3:
        Multiplicar()
    elif Opcion == 4:
        Dividir()
