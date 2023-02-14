def SumadeCubos(N):
    m=0
    while N>0:
        m=(N%10)**3+m
        N=N//10
    return m

def Seleccionar(modulo,*numeros):
    n=0
    for Nro in numeros:
        if Nro == SumadeCubos(Nro):
            print(Nro)

## *** PROGRAMA PRINCIPAL ****
Seleccionar(SumadeCubos,123,989,23,34,153)