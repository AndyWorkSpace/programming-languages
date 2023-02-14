# ************************  MÓDULO PATRÓN  **************************
# Modulo Operaciones
def Operaciones(lista):
    Suma=0
    Mayor=-1
    for i in range(0,len(lista)):
        # Calcular la suma de valores
        Suma=Suma+lista[i]
        # Determinar el mayor de la lista
        if Mayor<=lista[i]:
            Mayor=lista[i]
        else:
            Mayor
            
    return Suma,Mayor
        
# *******************  PROGRAMA PRINCIPAL  **************************
# Mostrar Las Operaciones
print("******* Resultados de las operaciones *****")
lista=[7,12,3466,25,100,212]
A,B=Operaciones(lista)
# Mostrar lista
print("Lista = ",lista)
# Mostrar la suma y el mayor de los valores
print("La suma de los valores es = ",A)
print("El mayor de los valores es = ",B)
