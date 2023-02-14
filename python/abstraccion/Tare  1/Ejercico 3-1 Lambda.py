## Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona y convierte
# algunos números a otro valor
#----Modulo Seleccionar y convertir
def SeleccionarConvertidor(Modulo,*Numeros):
    print("N\t 10%N")
    for Nro in Numeros:
        if Nro>500:
            print(Nro,"\t",Modulo(Nro))
            
# *******************  PROGRAMA PRINCIPAL  **************************
# Mostrar los impares
print('Números mayores a 500 con su 10%')
SeleccionarConvertidor(lambda N:N*0.1,784,1000,5000)
