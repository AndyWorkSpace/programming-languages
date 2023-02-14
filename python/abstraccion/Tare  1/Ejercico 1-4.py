## Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# a algun otro valor
def Seleccionar(S, *Numeros):
    for Nro in Numeros:
        if Nro==InvertirNumero(Nro):
            print(Nro)

def InvertirNumero(N):
    m=0
    while N>0:
        m=m*10+N%10
        N=N//10
    return m
        
# *******************  PROGRAMA PRINCIPAL  **************************
# Numero de digitos
print('Números capicuas')
Seleccionar(InvertirNumero,12,232,378,1010101,45,6886)

