def Menu():
    # -- Mostrar el menu de opciones
    print()
    print('*** ALUMNOS ***')
    print('1 Agregar')
    print('2 Consultar')
    print('3 Eliminar')
    print('4 Listar por Especialidad')
    print('5 Listar por Año')
    print('6 Listar (General)')
    print('7 FIn')

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
    CodLibro=input('Ingrese el codigo del Libro:')
    if Indice(CodLibro,Lista)>=0:
        print('Libro ya existe en la lista')
    else:
        # Ingresar la informacion del libro
        Titulo=input('Ingrese Titulo: ')
        Autor=input('Ingrese Autor: ')
        Anio=input('Ingrese Año: ')
        Especialidad=input('Ingrese la Especialidad: ')
        # Agregar a la lista
        Lista.append([CodLibro,Titulo,Autor,Anio,Especialidad])

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
def ListarGeneral(Lista):
    # -- Listar los Libros
    print()
    print('LISTADO DE LIBROS EN GENERAL')
    print('=======================================')
    print('Codigo\tTitulo\tAutor\tAño\tEspecialidad')
    print('--------\t----------\t-----------\t----------\t----------')
    for L in Lista:
        print(L[0], '\t', L[1], '\t', L[2], '\t', L[3], '\t', L[4])

# ----------- Listar Especialidad -------------
def ListarEspecialidad(Lista):
    n=input('Ingrese Especialidad:')
    # -- Listar los Libros
    print()
    print('LISTADO DE LIBROS POR ESPECIALIDAD')
    print('=======================================')
    print('Codigo\tTitulo\tAutor\tAño\tEspecialidad')
    print('--------\t----------\t-----------\t----------\t----------')
    for L in Lista:
        if L[4]==n:
            print(L[0], '\t', L[1], '\t', L[2], '\t', L[3], '\t', L[4])

# ----------- Listar POR AÑO -------------
def ListarAño(Lista):
    n=input('Ingrese Año del libro:')
    # -- Listar los Libros
    print()
    print('LISTADO DE LIBROS POR AÑO')
    print('=======================================')
    print('Codigo\tTitulo\tAutor\tAño\tEspecialidad')
    print('--------\t----------\t-----------\t----------\t----------')
    for L in Lista:
        if L[3]==n:
            print(L[0], '\t', L[1], '\t', L[2], '\t', L[3], '\t', L[4])

# ***************** PROGRAMA PRINCIPAL *******************
# -- Declarar la lista
Lista = []
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 7:
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
        ListarEspecialidad(Lista)
    elif Opcion == 5:
        ListarAño(Lista)
    elif Opcion == 6:
        ListarGeneral(Lista)
