## Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# a algun otro valor
def Convertidor(S, *Numeros):
    print("x\tF(x)")
    for Nro in Numeros:
        print(Nro,"\t",S(Nro))

# *******************  MÓDULOS DE LA APLICACIÓN  ********************

# Módulo para determinar el número de digitos
def NroDigitos(N):
    return len(str(N))

# *******************  PROGRAMA PRINCIPAL  **************************
# Mostrar los impares
print('Números y sus Números de digitos')
Convertidor(NroDigitos,1,2,3,4,5,6,7,8,9,10)
#:----------------------------------------------------------
'''# FORMA LAMBDA
print('Números y sus respectivos cuadrados')
Convertidor(lambda N:N**2,1,2,3,4,5,6,7,8,9,10)'''

