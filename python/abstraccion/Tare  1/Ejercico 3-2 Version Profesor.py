## Programa para Seleccionar y Convertir números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona y convierte numeros

# Modulo SeleccionarConvertir
def SeleccionarConvertidor(Modulo1,Modulo2,*Numeros):
    for Nro in Numeros:
        if Modulo1(Nro):
            print(Nro,"    ","Nro de digitos impares : ",Modulo2(Nro))

# Modulo Determinar 4 digitos
def CuatroDigitos(N):
    if len(str(N))==4:
        return N

# Modulo Numero de digitos Impares 
def DigitosImpares(N):
    NroImpares=0
    while N>0:
        if (N%10)%2!=0:
            NroImpares+=1 
        N=N//10
    return NroImpares
        
# *******************  PROGRAMA PRINCIPAL  **************************
# Mostrar los numeros de 4 cifras y el Nro de digitos impares
print("******* Numeros de 4 digitos *****")
SeleccionarConvertidor(CuatroDigitos,DigitosImpares,25,123,7840,5454,12345,100011)
