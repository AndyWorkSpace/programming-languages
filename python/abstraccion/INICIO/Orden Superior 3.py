## Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# a algun otro valor
def Convertidor(S, *Numeros):
    print("x\tF(x)")
    for Nro in Numeros:
        print(Nro,"\t",S(Nro))

# *******************  MÓDULOS DE LA APLICACIÓN  ********************

# Módulo para determinar el cuadrado de un numero
def Cuadrado(N):
    return N**2

# Módulo para determinar el cubo de un numero
def Cubo(N):
    return N**3
# Modulo para determinar la raiz de un numero
def Raiz(N):
    return N**0.5

# *******************  PROGRAMA PRINCIPAL  **************************
# Mostrar los impares
print('Números y sus respectivos cuadrados')
Convertidor(Cuadrado,1,2,3,4,5,6,7,8,9,10)
