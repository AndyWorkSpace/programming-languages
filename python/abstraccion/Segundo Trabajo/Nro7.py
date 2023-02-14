'''
En una estructura de tipo diccionario se almacenó la información de los proyectos de
 investigación de la Escuela Profesional de Ingeniería Informática y de sistemas. 
 En el atributo “clave” se tiene el código del proyecto, mientras que el atributo “valor” 
 se tiene una lista con los siguientes datos: Nombre, LineaInvestigacion, 
 NroInvestigadores y Presupuesto. Escribir módulos para:
- Determinar el número de investigadores de un determinado proyecto.
- Determinar el proyecto con el mayor presupuesto.
- Generar una lista con los nombres de los proyectos de una determina Línea de investigación.

cod proyecto : , linea investifacion, nori investigfa, presupesti
'''

# modulo numero de investigaciones de un determiinado proyecto
def NumeroInvestigadores(D):
    # pedir el codigo del proyecto
    n=int(input('Ingrese el codigo del proyecto:'))
    if n in D:
        # retornar numero de investigadores
        return D[n][2]

# modulo el proyecto con el mayor presupuesto
def ProyectoMasPresupuesto(dic):
    # variable auxiliar mayor
    temp=0
    for k,v in dic.items():
        # comprarar presupuestos
        if v[3]>temp:
            temp=v[3]
    # retornar mayor presupuesto
    return temp

# modulo lista con los nombres de los proyectos de una determinadad linea de investigacion    
def ProyectoMismaLI(dic):
    # lista Nombre de proyectos
    lisname=[]
    LineaInvestigacion=str(input("Ingrese la linea de investigacion: "))
    for k,v in dic.items():
        if v[1]==LineaInvestigacion:
            # agregar nombres de proyectos
            lisname.append(v[0])
    # retonar listas nombre de proyectos
    return lisname

