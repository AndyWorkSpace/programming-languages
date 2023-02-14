'''
Se tiene una relacon de Nalumnos,. Para cada uno de ellos se tiene 3 niotas
Escirbir una alpiccaion que permita registrar en un lista dicha informaaciom,
luego, que muestre la relacion de alumno, con sus respectivas notas y el promedio'''
#from LibreriaListas import *

# ******* MODULOS ESPECIFICOS DE LA APLICACION ******

# ------ menu ------
def Menu():
    # -- Mostrar el mendu de opciones
    print()
    print('*** ALUMNOS ***')
    print('1 Agregar')
    print('2 Consultar')
    print('3 Eliminar')
    print('4 Listar')
    print('5 Listar aprobados')
    print('6 Fin')

# -------- AGREGAR ------------
def Posicion(Codigo,Lista):
    P=-1
    K=-1
    for LA in Lista:
        K+=1
        if Codigo in LA:
            P=K
            break
    return P

# ------- Agregar ------------
def Agregar(Lista):
    #-- Leer el codigo del alumno
    CodAlumno=input('Ingrese el codigo del alumno:')
    if Posicion(CodAlumno,Lista)>=0:
        print('Codigo ya existe en la lista')
    else:
        # Ingresar las notas
        Nota1=int(input('Ingrse Nota 1:'))
        Nota2=int(input('Ingrse Nota 2:'))
        Nota3=int(input('Ingrse Nota 3:'))
        # Agregar a la lista
        Lista.append([CodAlumno,Nota1,Nota2,Nota3])

# ---- Consultar ----------
def Consultar(Lista):
    # -- Leer el valor de la carrera
    Codigo=input('Ingrese el codigo del alumno:')
    P=Posicion(Codigo,Lista)
    if P>=0:
        print(Lista[P])
    else:
        print(Codigo,' no esta en la lista')

# ----------- Eliminar -------------
def Eliminar(Lista):
    # -- Leer el codigo del alumno
    Codigo = input('Ingrese el código del alumno:')
    P = Posicion(Codigo, Lista)
    if P >= 0:
        del Lista[P]
    else:
        print(Codigo, ' no está en la lista')

# ----------- Listar -------------
def Listar(Lista):
    # -- Listar los alumnos
    print()
    print('LISTADO DE ALUMNOS')
    print('=================')
    print('Codigo\tNota1\tNota2\tNota3\tPromedio')
    print('------\t-----\t-----\t-----\t--------')
    for A in Lista:
        Prom = (A[1] + A[2] + A[3])/3
        print(A[0], '\t', A[1], '\t', A[2], '\t', A[3], '\t', Prom)


# ***************** PROGRAMA PRINCIPAL *******************
# -- Declarar la lista
Lista = []
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 6:
    # -- Mostrar menu
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción --> '))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        Agregar(Lista)
    elif Opcion == 2:
        Consultar(Lista)
    elif Opcion == 3:
        Eliminar(Lista)
    elif Opcion == 4:
        Listar(Lista)
    elif Opcion == 5:
        ListarAprobados(Lista)