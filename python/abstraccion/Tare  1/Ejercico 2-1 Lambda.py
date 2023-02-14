## Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# a algun otro valor
def Convertidor(S, *Numeros):
    print("x\tNumero de digitos")
    for Nro in Numeros:
        print(Nro,"\t",S(Nro))

# *******************  PROGRAMA PRINCIPAL  **************************
# Numero de digitos
print('Números y sus Números de digitos')
Convertidor(lambda N:len(str(N)),12,232,3,4,45,68787)

