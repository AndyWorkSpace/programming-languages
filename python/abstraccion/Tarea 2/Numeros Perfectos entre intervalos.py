
def EsNumeroPer(N):
    m=0
    for i in range(1,N):
        if N%i==0:
            m=m+i
    return m

def NumeroPer(N,Nmin):
    if N>=Nmin:
        NumeroPer(N-1,Nmin)
        if N==EsNumeroPer(N):
            print (N, end=' ')

#************ PROGRAMA PRINCIPAL **********#
# LEER LIMITES
LimiteMenor=int(input("Ingrese el limite menor: "))
LimiteMayor=int(input("Ingrese el limite mayor: "))
# Mostrar numero perfectos

NumeroPer(LimiteMayor,LimiteMenor)

