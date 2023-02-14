'''
Se tiene una relación de N alumnos. Para cada uno de ellos se tiene 3 notas.
Escribir una aplicación que permita registrar en una lista dicha información,
luego, que muestra la relación de alumnos, con sus respectivas notas y el promedio.
'''
#from LibreriaListas import *
# ************ MÓDULOS ESPECÍFICOS DE LA APLICACIÓN ***************
# ----------- Menu -------------
# ------ menu ------
def Menu():
    # -- Mostrar el mendu de opciones
    print()
    print('*** ALUMNOS ***')
    print('1 Agregar')
    print('2 Consultar')
    print('3 Eliminar')
    print('4 Listar')
    print('5 Listar Aprobados')
    print('6 Listar Desaprobados')
    print('7 Listar Reprobados')
    print('8 Fin')

# ----------- Índice -------------
def Indice(Codigo, Lista):
    # -- Recuperar lista solo de códigos
    LCodigos = [A[0] for A in Lista]
    # -- Verificar si código existe en la lista de códigos
    if Codigo in LCodigos:
        return LCodigos.index(Codigo)
    else:
        return -1

# ------- Agregar ------------
def Agregar(Lista):
    #-- Leer el codigo del alumno
    CodAlumno=input('Ingrese el codigo del alumno:')
    if Indice(CodAlumno,Lista)>=0:
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
    I=Indice(Codigo,Lista)
    if I>=0:
        print(Lista[I])
    else:
        print(Codigo,' no esta en la lista')

# ----------- Eliminar -------------
def Eliminar(Lista):
    # -- Leer el codigo del alumno
    Codigo = input('Ingrese el código del alumno:')
    I = Indice(Codigo, Lista)
    if I >= 0:
        del Lista[I]
    else:
        print(Codigo, ' no está en la lista')

# ----------- Listar -------------
def TablaListar(titulo,Lista, Modulo):
    # -- Poner títulos y rótulos
    print()
    print('LISTADO DE ALUMNOS '+titulo)
    print('=================')
    print('Codigo\tNota1\tNota2\tNota3\tPromedio')
    print('------\t-----\t-----\t-----\t--------')
    # -- Recuperar lista de alumnos, incluyendo el promedio
    ListaPromedio = [[A[0],A[1],A[2],A[3],(A[1]+A[2]+A[3])/3] for A in Lista]
    # -- Mostrar listado
    for A in ListaPromedio:
        if Modulo(A):
            print(A[0], '\t', A[1], '\t', A[2], '\t', A[3], '\t', A[4])


# ***************** PROGRAMA PRINCIPAL *******************
# -- Declarar la lista
Lista = []
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 8:
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
        TablaListar('PROMEDIO',Lista,lambda x : x[4])
    elif Opcion == 5:
        TablaListar('APROBADOS',Lista, lambda x : x[4] >= 13.5)
    elif Opcion == 6:
        TablaListar('DESAPROBADOS',Lista, lambda x : 9 < x[4] <= 13.5)
    elif Opcion == 7:
        TablaListar('REPROBADOS',Lista, lambda x : x[4] <= 9)