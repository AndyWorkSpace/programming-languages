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

def MCD(lista):
    for i in range(0,len(lista)-1):
        R=lista[i]%lista[i+1]
        while R!=0:
            lista[i]=lista[i+1]
            lista[i+1]=R
            R=lista[i]%lista[i+1]
        return lista[i+1]
        
# *******************  PROGRAMA PRINCIPAL  **************************
# Mostrar La lista
print("******* Resultados de las operaciones *****")
lista=[7,12,3466,25,100,212]
A,B=Operaciones(lista)
C=MCD(lista)
# Mostrar lista
print("Lista = ",lista)
# Mostrar la suma y el mayor de los valores
print("La suma de los valores es = ",A)
print("El mayor de los valores es = ",B)
print("MCD de los valores = ",C)
