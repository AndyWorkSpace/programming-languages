#-----------Menu-----------
def Menu():
    #-- Mostrar el menu de opciones
    print()
    print('*** Carreras Profesionales ***')
    print('1 Agregar')
    print('2 Buscar')
    print('3 Modificar')
    print('4 Eliminar')
    print('5 Listar')
    print('6 FIN')

#-------Agregar--------
def Agregar(D):
    #-- leer el valor de la clave
    Clave=input('Ingrese el codigo de la carrera Profesional:')
    if Clave in D:
        print(Clave,' ya existe en la base de datos')
    else:
        Valor=input('Ingrese el nombre de la carrera Profesional:')
        #-- agregar en el diccionario
        D[Clave]=Valor

# ------------ Buscar -------
def Buscar(D):
    # -- leer el valor de la clave
    Clave=input('Ingrese el codigo de la carrera profesional:')
    if Clave in D:
        print(Clave,':',D[Clave])
    else:
        print('No existe en la base de datos')

#--------- Modificar--------
def Modificar(D):
    #-- leer el valor de la clave
    Clave=input('Ingrese el codigo de la carrera Profesional:')
    if Clave in D:
        #-- Mostrar el actual valor
        print(Clave,' tiene actualmente el valor de ',D[Clave])
        #-- leer el valor a cambiar
        Valor=input('Ingrese el nombre de la Carreta Profesioanl con el que sea cambiar:')
        #-- modificar el diccionario
        D[Clave]=Valor
    else:
        print(Clave,'No existe en la base de datos')

#--------- Eliminar -----------
def Eliminar(D):
    #-- leer el valor de la clave
    Clave=input('Ingrese el codigo de la carrera Profesional:')
    if Clave in D:
        del D[Clave]
    else:
        print(Clave,'No existe en la base de datos')

#--------- Listar ---------------
def Listar(D):
    #-- Listar los elementos del Diccionario
    print()
    print('LOS ELEMENTOS DEL DICCIONARIO SON:')
    print('=================================')
    print('Codigo Carrera Profesional\tNombre Carrera Profesional')
    print('--------------------------\t----------------')
    for K,V in D.items():
        print(K,'\t'*4,V)

#*************** PROGRAMA PRINCIPAL ***********
D={}
#--Mostrar y procesar Menu
Opcion=0
while Opcion!=6:
    #-- Mostrar menu
    Menu()
    #-- Leer opcion
    Opcion=int(input('Ingrese opcion-->'))
    #-- Procesar deacuerdo a la opcion
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
