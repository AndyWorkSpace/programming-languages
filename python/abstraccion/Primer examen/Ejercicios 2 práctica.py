# Módulo seleccionar de Angelito
def SeleccionarAngelito(*Nros):
    # Tomar un numero de los numeros brindados
    for N in Nros:
        # Analizar el Número de divisores
        if NumeroDivisores(N)==6:
            print('Angelito dice que ',N,' ES un número de la suerte')
        else:
            print('Angelito dice que ',N,' NO es un número de la suerte')

# Modulo calcular el número de divisores
def NumeroDivisores(N):
    #--Variable acumuladora de # de divisores
    NumDiv=0
    #--Calcular cuántos divisores tiene
    for i in range(1,N+1):
        if N%i==0:
            #--Sumar 1 si es divisor de N
            NumDiv=NumDiv+1
            
    #--Retornar el Número de divisores
    return NumDiv
#*************** PROGRAMA PRINCIPAL ****************"
# Mostrar los números de la suerte según a una lista de números
SeleccionarAngelito(199,20,123,12,7,465)
