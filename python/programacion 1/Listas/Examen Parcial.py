''' Código, Provincia donde vive, 
Distrito donde vive y dispositivo (Desktop, Laptop o Celular) que utiliza para realizar sus clases virtuales.'''
 
 
#******************* MÓDULOS *********************#
# ---------- Módulo Menú ---------------
def Menu():
    # -- Mostrar el menú de opciones
    print()
    print('*** Estudiantes ***')
    print('1 Agregar')
    print('2 Listar estudiantes que no viven en Cusco')
    print('3 Número de estudiantes con cada dispositivo ')
    print('4 Fin')
 
 
 
# ----------- Módulo Índice -------------
def Indice(Codigo, Lista):
    # -- Recuperar lista solo de códigos
    LCodigos = [A[0] for A in Lista]
    # -- Verificar si código existe en la lista de códigos
    if Codigo in LCodigos:
        return LCodigos.index(Codigo)
    else:
        return -1
 
# ------- Módulo Agregar Estudiante ------------
def AgregarEstudiante(Lista):
    #-- Leer el codigo del alumno
    CodAlumno=input('Ingrese el código del alumno:')
    while len(CodAlumno)!=6:
        CodAlumno=input('ERROR.. Ingrese el código del alumno(6 dígitos):')
    if Indice(CodAlumno,Lista)>=0:
        print('Codigo ya existe en la lista')
    else:
        # Ingresar datos del estudiante
        Provincia=input('Ingrese Provincia donde vive :')
        Distrito=input('Ingrese Distrito donde vive :')
        Dispositivo=input('Ingrese Dispositivo que use para sus clases(Desktop, Laptop o Celular) :')
        # Agregar a la lista
        Lista.append([CodAlumno,Provincia,Distrito,Dispositivo])
 
#------- Módulo Alumnos que no radican en la provincia de cusco
def AlumnosNoCusco(lista):
    print('**** Estudiantes que no radican en Cusco ****')
    print('CODIGO/PROVINCIA/DISTRITO/DISPOSITIVO')
    #-- Analizar la provincia de cada estudiante
    for L in lista:
        #-- Verificar que no viva en cusco
        if L[1].upper()!='CUSCO':
            #-- Mostrar los datos del estudiante que no vive en Cusco
            print(L)
 
 
 
#------ Módulo número de dispositivos usados
def NroDispositivos(Lista):
    #-- Determinar lista de Dispositivos
    LD=[]
    for L in Lista:
        #-- Verificar que no se repita en la lista de dispositivos
        if L[3] not in LD:
            #-- Agregar nuevo dispositivo
            LD += [L[3]] 
    
    #-- Contar el número de dispositivos usados por los estudiantes
    LNPC=[[D,len([L for L in Lista if L[3] == D])] for D in LD]
    #-- Mostrar el dispositivo y el número de estudiantes que la usan
    for E in LNPC:
        print('Estudiantes con ',E[0],':',E[1])
 
# ***************** PROGRAMA PRINCIPAL *******************
# -- Declarar la lista
Lista = []
# -- Mostrar y procesar Menú
Opcion = 0
while Opcion != 4:
    # -- Mostrar menu
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción --> '))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        AgregarEstudiante(Lista)
    elif Opcion == 2:
        AlumnosNoCusco(Lista)
    elif Opcion == 3:
        NroDispositivos(Lista)
