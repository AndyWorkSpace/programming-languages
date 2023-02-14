'''
La Dirección Regional de Salud (DIRESA) del departamento del Cusco, puso 
a disposición de la comunidad los datos de la pandemia. Uno de los integrantes
 del equipo informático de La DIRESA, registró en un diccionario PYTHON la
  relación de los distritos del departamento del Cusco con su correspondiente 
  
  número de contagiados. A Ud. Se le pide escribir módulos PYTHON para:
1.- Determinar los distritos con el mayor y menor número de contagiados.
2.- Generar una lista con los distritos en los que se debe implantar un cerco 
epidemiológico, es decir los distritos con más de 1000 contagiados.

'''


# **** Modulo Mayores y Menores contagios ****    
def MenorContagios(D):
    mayorContagios=-1
    for key in D:
        if D[key] >= mayorContagios:
            mayorContagios=D[key]
    return mayorContagios

def MayorContagios(D):
    menorContagios=999999999
    for key in D:
        if D[key]<=menorContagios:
            menorContagios=D[key]
    return menorContagios


# ****   Modulo Distritos con mas de 1000 contagios ****  
def CidudadEpidemiologicas(D):
    DistritosMas1000=[]
    for k in  D:
        if D[k]>1000:
            DistritosMas1000.append(k)
    return DistritosMas1000
    
D={'A':12686,'B':24,'C':8000,'D':347787,'E':4,'F':6666666}
a,b=MenorMayorContagios(D)
print(a,b)
print(CercoEpidemiologico(D))