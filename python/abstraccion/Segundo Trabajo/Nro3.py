'''2.- En una Lista se tiene la relación de los alumnos matriculados en la asignatura de Abstracción de Datos y Objetos; en otra Lista se tiene la relación de los alumnos matriculados en la asignatura de Programación I. Escribir módulos para:
- Mostrar la relación de alumnos que estén matriculados en ambas asignaturas.
- Generar un arreglo con la relación de los alumnos que estén matriculados en Abstracción de Datos y Objetos, y no estén en Programación I.

'''
# Modulo alumnos que pertenecen a Abs y Programacion I
def AlumnosRepetidos(LA,LB):
    # crear lista de alumnos que llevan ambos cursos
    ListaR=[]
    for i in LA:
        if i in LB:
            # agregar alumnos
            ListaR.append(i)
    return ListaR
# Modulo alumnos que pertenecen a Abs y no a Programacion I
def AlumnosAbsMenosProgra(LA,LB):
    # Crear lista de alumnos q esten en abs y no en progra I
    ListaMenos=[]
    for i in LA:
        if i not in LB:
            # agregar alumnos a la nueva lista
            ListaMenos.append(i)
    return ListaMenos


