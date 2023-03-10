'''
Escribir una aplicación para gestionar Alumnos
'''
# ************ MÓDULOS ESPECÍFICOS DE LA APLICACIÓN ***************
# ----------- Menu -------------
def Menu():
    # -- Mostrar el menú de opciones
    print()
    print('***** ALUMNOS *****')
    print('1 Agregar')
    print('2 Buscar')
    print('3 Modificar')
    print('4 Eliminar')
    print('5 Listar')
    print('6 FIN')

# ----------- Leer Alumno -------------
def LeerAlumno():
    # -- Leer los datos del Alumno
    A = []
    A += [input('Apellido paterno: ')]
    A += [input('Apellido materno: ')]
    A += [input('Nombres: ')]
    A += [input('Carrera Profesional: ')]
    # -- retornar valores de Alumno
    return A

# ----------- Escribir Alumno -------------
def EscribirAlumno(Codigo, Datos):
    # -- Escribir los datos de la Alumno
    print()
    print('Código: ',Codigo)
    print('Apellido paterno: ',Datos[0])
    print('Apellido materno: ',Datos[1])
    print('Nombres: ',Datos[2])
    print('Carrera Profesional: ',Datos[3])

# ----------- Agregar -------------
def Agregar(D):
    # -- Leer el valor clave
    print()
    print('Ingrese los datos del Alumno')
    Clave = input('Código: ')
    if Clave in D:
        print(Clave,' ya existe en la Base de datos')
    else:
        # -- Leer los datos del Alumno
        Valor = LeerAlumno()
        # -- Agregar al diccionario
        D[Clave] = Valor

# ----------- Buscar -------------
def Buscar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código del Alumno: ')
    if Clave in D:
        EscribirAlumno(Clave, D[Clave])
    else:
        print(Clave, 'No existe en la base de datos')

# ----------- Modificar -------------
def Modificar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código del Alumno: ')
    if Clave in D:
        # -- Mostrar el actual valor
        print(Clave,' tiene actualmente los siguientes valores')
        EscribirAlumno(Clave, D[Clave])
        # -- Leer los nuevos valores
        print()
        print('Ingrese los nuevos datos del Alumno')
        Valor = LeerAlumno()
        # -- Modificar el diccionario
        D[Clave] = Valor
    else:
        print(Clave, 'No existe en la base de datos')

# ----------- Eliminar -------------
def Eliminar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código del Alumno a eliminar:')
    if Clave in D:
        del D[Clave]
    else:
        print(Clave, 'No existe en la base de datos')

# ----------- Listar -------------
def Listar(D):
    # -- Listar los elementos del diccionario
    print()
    print('RELACIÓN DE ALUMNOS')
    print('===================')
    for K, V in D.items():
        EscribirAlumno(K, V)

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