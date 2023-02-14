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
def MenorMayorContagios(D):
    # auxiliares
    mayorContagios=-1
    menorContagios=999999999
    # Comparar numero de contagios en cada distrito
    for key in D:
        # Actualizar el mayor numero de contagios
        if D[key] >= mayorContagios:
            mayorContagios=D[key]
        else:
            # Actualizar el menor numero de contagios
            if D[key] <= menorContagios:
                menorContagios=D[key]
    # Retornar Mayor y Menor numero de contagios
    return mayorContagios,menorContagios

# ****   Modulo Distritos con mas de 1000 contagios ****  
def CercoEpidemiologico(D):
    # Crear lista de Distritos en peligro
    DistritosEnPeligro=[]
    # Comparar numero de contagios que sean mayores a 1000
    for k in  D:
        if D[k]>1000:
            # Agregar distriro con mas de 1000 contagios
            DistritosEnPeligro.append(k)
    # Retornar lista de Distritos con mas de 1000 contagios
    return DistritosEnPeligro
    
D={'A':12686,'B':24,'C':8000,'D':347787,'E':4,'F':6666666}
a,b=MenorMayorContagios(D)
print(a,b)
print(CercoEpidemiologico(D))