'''
En una estructura de tipo diccionario se tiene la relación de asignaturas con su
 respectiva nota, cursadas por un estudiante de la escuela profesional de ingeniería informática 
 y de sistema. En otro diccionario se tiene la relación de asignaturas con su respectivo número de créditos.
  Escribir un módulo que calcule el número de créditos acumulados por dicho estudiante.
'''
D1={192422:{'IF451AIN':16,'ME351AIN':14,'FI370CIN':5}}
D2={'IF451AIN':4,'FI370CIN':4,'ME351AIN':4}

# Modulo Numero de creditos acumulados por el estudiante
def CreditosAcumulados(D1,D2):
  # lista de cursos aprobados
  CursosAprobados=[]
  # clave igual codigo del alumno
  for key1 in D1:
    # clave igual a los codigos de las asignaturas en el valor
    for key2 in D1[key1]:
      # comparar notas del valor de key2
      if D1[key1][key2] >= 13.5:
        # agregar cursos aprobados
        CursosAprobados.append(key2)
  # acumulador de creditos
  totalCreditos=0
  for Cursos in CursosAprobados:
    # buscar codigos de cursos en D2 y sumar los creditos respectivos
    if Cursos in D2:
      # sumar creditos de los curos aprobados
      totalCreditos=totalCreditos+D2[Cursos]
  # retornat total de creditos
  return totalCreditos

print(CreditosAcumulados(D1,D2))
