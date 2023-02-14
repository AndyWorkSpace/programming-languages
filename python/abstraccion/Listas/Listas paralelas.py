# EJEMPLO DE LISTAS PARALELAS
def LeerNotas():
    #-- Leer numero de notas
    n=int(input('Ingrese numero de alumnos:'))
    #-- Leer codigo y nota de cada alumno
    Lcod=[]
    Lnot=[]
    for k in range(0,n):
        codigo=int(input('Ingrese codigo '+str(k+1)+':'))
        nota=int(input('Ingrese nota '+str(k+1)+':'))
        Lcod=Lnot+[codigo]
        Lnot=Lnot+[nota]
    #-- devolver los codigos y las notas
    return Lcod,Lnot

# PROGRAMA PRINCIAPL
Lcodigos,Lnotas=LeerNotas()
for k in range(0,len(Lcodigos)):
    print('Alumno ',k+1,  Lcodigos[k],Lnotas[k])