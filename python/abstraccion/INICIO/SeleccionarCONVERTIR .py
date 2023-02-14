## Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# a algun otro valor
def SeleccionarConvertidor(S,C,*Numeros):
    print("x\tF(x)")
    for Nro in Numeros:
        if S(Nro):
            print(Nro,"\t",C(Nro))
# *******************  PROGRAMA PRINCIPAL  **************************
def EsImpar(N):
    return N%2!=0

def Cuadrado(N):
    return N**2

# Mostrar los impares
print('Números y sus respectivos cuadrados')
SeleccionarConvertidor(EsImpar,Cuadrado,1,2,3,4,5,6,7,8,9,10)
