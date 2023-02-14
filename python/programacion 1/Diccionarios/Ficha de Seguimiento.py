'''
Escribir una aplicación para gestionar Asignaturas
'''
# ************ MÓDULOS ESPECÍFICOS DE LA APLICACIÓN ***************
# ----------- Menu -------------
def Menu():
    # -- Mostrar el menú de opciones
    print()
    print('***** ASIGNATURAS  *****')
    print('1 Agregar')
    print('2 Buscar')
    print('3 Modificar')
    print('4 Eliminar')
    print('5 Listar')
    print('6 FIN')

# ----------- Leer Alumno -------------
def LeerAsignatura():
    # -- Diccionario de asignaturas
    A = {}
    # -- Leer asignaturas y notas
    Resp='S'
    while Resp!='N':
        CodAsig = input('Ingrese código de asignatura: ')
        NotaAsig = input('Ingrese la respeciva nota:')
        A[CodAsig]=NotaAsig
        # -- Agregar más asignaturas depende a la respuesta
        Resp= input('¿Hay más asignaturas <S> o <N>?:')
    # -- retornar valores del Alumno
    return A

# ----------- Escribir Alumno -------------
def EscribirAsignatura(Codigo, Datos):
    # -- Escribir los datos de la Alumno
    print()
    print('FICHA DE SEGUIMIENTO DEL ALUMNO:',Codigo)
    print('==================================')
    print('Asignatura\t\tNota')
    for M,N in Datos.items():
        print(M,'\t'*2,N)

# ----------- Agregar -------------
def Agregar(D):
    # -- Leer el valor clave
    print()
    Clave = input('Ingrese codigo del alumno: ')
    if Clave in D:
        print(Clave,' ya existe en la Base de datos')
    else:
        # -- Leer los datos del Alumno  
        Valor = LeerAsignatura()
        # -- Agregar al diccionario
        D[Clave] = Valor

# ----------- Buscar -------------
def Buscar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código del alumno: ')
    if Clave in D:
        EscribirAsignatura(Clave, D[Clave])
    else:
        print(Clave, 'No existe en la base de datos')

# ----------- Modificar -------------
def Modificar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código deL alumno: ')
    if Clave in D:
        # -- Mostrar el actual valor
        print(Clave,' tiene actualmente los siguientes valores')
        EscribirAsignatura(Clave, D[Clave])
        # -- Leer los nuevos valores
        print()
        print('Ingrese los nuevos datos de las Asignaturas')
        Valor = LeerAsignatura()
        # -- Modificar el diccionario
        D[Clave] = Valor
    else:
        print(Clave, 'No existe en la base de datos')

# ----------- Eliminar -------------
def Eliminar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código del alumno: ')
    if Clave in D:
        del D[Clave]
    else:
        print(Clave, 'No existe en la base de datos')

# ----------- Listar -------------
def Listar(D):
    # -- Listar los elementos del diccionario
    print()
    print('FICHAS DE SEGUIMIENTO')
    print('===================')
    for K, V in D.items():
        print('FICHA DE SEGUIMIENTO DEL ALUMNO:',K)
        print('==================================')
        print('Asignatura\t\tNota')
        for M,N in V.items():
            print(M,'\t'*2,N)

# ***************** PROGRAMA PRINCIPAL *******************
# -- Declarar el diccionario
D = {}
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 6:
    # -- Mostrar menu
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción -->'))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        Agregar(D)
    elif Opcion == 2:
        Buscar(D)
    elif Opcion == 3:
        Modificar(D)
    elif Opcion == 4:
        Eliminar(D)
    elif Opcion == 5:
        Listar(D)