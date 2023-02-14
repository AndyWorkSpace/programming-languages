## Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# a algun otro valor
def SeleccionarConvertidor(Modulo,*Numeros):
    print("N\t 10%N")
    for Nro in Numeros:
        if Modulo(Nro):
            print(Nro,"\t",Modulo(Nro))
# *******************  PROGRAMA PRINCIPAL  **************************
def Muestra(N):
    if N>500:
        return N*0.1

# Mostrar los impares
print('Números mayores a 500 con su 10%')
SeleccionarConvertidor(Muestra,499,784,1000,5000,9999,100000)
