def LeerAlumnos():
    #-- Leer numero de alumnos
    n=int(input('Ingrese numero de alumnos:'))
    #-- Leer datos del alumno
    L=[]
    for k in range(0,n):
        LD=[]
        codigo=input('Ingrese codigo '+str(k+1)+':')
        Nombres=input('Ingrese nombres '+str(k+1)+':')
        Escuela=input('Ingrese escuela '+str(k+1)+':')
        LD=[codigo,Nombres,Escuela]
        L=L+[LD]
    #-- devolver los codigos y las notas
    return L


def MostrarAlumnosPorCarrera(L):
    #-- determinar lista de carreras
    LC=[]
    for A in L:
        if A[2] not in LC:
            LC +=[A[2]]
    
    #-- Contar el numero de alumnos de cada carrera
    LNPC=[[C,len([A for A in L if A[2]==C])]for C in LC]
    #-- Mostrar carreras y el numero de alumnos
    for E in LNPC:
        print(LNPC[0],LNPC[1])

#******************* Programa Principal******************
LAlumnos=LeerAlumnos()
for k in range(0,len(LAlumnos)):
    print('Alumno ',k+1,LAlumnos[k])

'''print('Relacion de alumnos de ingenieria informatica')
LIN=[A[0:4] for A in LAlumnos if A[4]=='IN']
for k in range(0,len(LIN)):
    print('Alumno ',k+1,':',LIN[k])'''

print('mostrar cuantos alumnos hay en cada carrera')
MostrarAlumnosPorCarrera(LAlumnos)

