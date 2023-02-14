## Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# a algun otro valor
def Convertidor(S, *Numeros):
    print("x\tNumero de digitos")
    for Nro in Numeros:
        print(Nro,"\t",S(Nro))

def InvertirNumero(N):
    m=0
    while N>0:
        m=m*10+N%10
        N=N//10
    return m
        
# *******************  PROGRAMA PRINCIPAL  **************************
# Numero de digitos
print('Números y sus Números de digitos')
Convertidor(InvertirNumero,12,232,3,4,45,68787)

