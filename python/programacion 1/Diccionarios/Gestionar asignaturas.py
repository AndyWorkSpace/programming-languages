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
    # -- Leer los datos del Alumno
    A = {}
    Resp='S'
    while Resp!='N':
        CodAsig = input('Ingrese código de asignatura: ')
        NotaAsig = input('Ingrese la respeciva nota:')
        A[CodAsig]=NotaAsig
        Resp= input('¿Hay más asignaturas <S> o <N>?')
    # -- retornar valores de Alumno
    return A

# ----------- Escribir Alumno -------------
def EscribirAsignatura(Codigo, Datos):
    # -- Escribir los datos de la Alumno
    print()
    print('Código: ',Codigo)
    print('Nombre: ',Datos[0])
    print('Categoría: ',Datos[1])
    print('Créditos: ',Datos[2])

# ----------- Agregar -------------
def Agregar(D):
    # -- Leer el valor clave
    print()
    print('Ingrese los datos de la Asignatura')
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
    Clave = input('Ingrese el código de la Asignatura: ')
    if Clave in D:
        EscribirAsignatura(Clave, D[Clave])
    else:
        print(Clave, 'No existe en la base de datos')

# ----------- Modificar -------------
def Modificar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código de la Asignatura: ')
    if Clave in D:
        # -- Mostrar el actual valor
        print(Clave,' tiene actualmente los siguientes valores')
        EscribirAsignatura(Clave, D[Clave])
        # -- Leer los nuevos valores
        print()
        print('Ingrese los nuevos datos de la Asignatura')
        Valor = LeerAsignatura()
        # -- Modificar el diccionario
        D[Clave] = Valor
    else:
        print(Clave, 'No existe en la base de datos')

# ----------- Eliminar -------------
def Eliminar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código de la asignatura a eliminar: ')
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
        print(V)


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