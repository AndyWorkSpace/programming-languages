#Modulo seleccionador
def Seleccionador(modulo,*Numeros):
    for elem in Numeros:
        if modulo(elem):
            print("Es un numero perfecto =",elem)

# Modulo para determinar si es un numero perfecto
def NroPerfecto(P):
    x=0
    for i in range (1,P):
        if P%i ==0:
            x=x+i
    if x==P:
        return x

#****************Programa principal***************
# Mostrar Numeros perfectos
Seleccionador(NroPerfecto,25,6,12,25,28,496,8128)
