## Programa para Seleccionar números

# ************************  MÓDULO PATRÓN  **************************

# Dado un conjunto de números, este módulo selecciona algunos números

# Modulo Seleccionar

def SeleccionarConvertidor(Modulo,*Numeros):
    for Nro in Numeros:
        if Modulo(Nro):
            print(Nro,"    ","Nro de digitos impares : ",Modulo(Nro))

def DigitosImpares(N):
    if len(str(N))==4:
        NroImpares=0
        while N>0:
            if (N%10)%2!=0:
                NroImpares+=1 
            N=N//10
        return NroImpares
        
# *******************  PROGRAMA PRINCIPAL  **************************
# Mostrar los numeros de 4 cifras y el Nro de digitos impares
print("Numeros de 4 digitos ")
SeleccionarConvertidor(DigitosImpares,25,123,7840,12345,100011)
