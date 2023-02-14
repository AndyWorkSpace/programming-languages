
#************* MODULOS ESPECIFICOS DE LA APLICACION *******
#--- menu--
def Menu():
    print('*** ALUMNOS   ***')
    print('1 -->Agregar alumno y notas')
    print('2 -->Mostrar alumnos y notas')
    print('3 -->Mostrar alumnos y promedios')

#------- agregar alumno-------
def AgregarAlumno(DA):
    #-- leer el codigo del alumno
    Codigo=input('Ingrese el codigo:')
    #-- Leer las notas del alumno
    Notas=[]
    for k in range(1,5):
        Nota=float(input('Ingrese nota '+str(k)+':'))
        Notas+=[Nota]
    #-- agregar al diccionario
    DA[Codigo]=Notas

#--------- Mostrar alumnos y notas-------
def MostrarAlumnosNotas(DA):
    #--- Mostrar alumnos y sus respectivvas notas
    print('*** Lista de alumnos y notas')
    for Codigo,Notas in DA.items():
        print(Codigo,Notas)
    print('')
    '''for Codigo in DA:
        print(Codigo, DA[Codigo])'''

#--------- Mostrar alumnos y promedios-------
def MostrarAlumnosPromedios(DA):
    # -- Mostrar alumnos y sus respectivas notas
    print('*** LISTADO DE ALUMNOS Y Promedios ***')
    for Codigo, Notas in DA.items():
        Suma = 0
        for Nota in Notas:
            Suma += Nota
        print(Codigo, Suma/len(Notas))
    print('')
    
# ***************** PROGRAMA PRINCIPAL *******************
# -- Declarar diccionario
DA = {}
# -- Mostrar y procesar Menú
Opcion = 0
while Opcion < 4:
    # -- Mostrar Menú
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción: '))
    # -- Procesar cada opcion del menu
    if (Opcion == 1):
        AgregarAlumno(DA)
    elif (Opcion == 2):
        MostrarAlumnosNotas(DA)
    elif (Opcion == 3):
        MostrarAlumnosPromedios(DA)
