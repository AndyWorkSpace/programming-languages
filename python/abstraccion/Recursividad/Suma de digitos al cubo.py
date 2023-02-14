'''
def SumaCubos(N):
    if N<10:
        return N**3
    else:
        return (N%10)**3 + SumaCubos(N//10)

N=int(input("Ingrese un numero = "))
print((N,"Es un numero espacial")if N==SumaCubos(N) else "No es numero espacial")
'''

def EsNumeroEspecial(N):
    U=N%10
    D=(N//10)%10
    C=N//100
    return N== U**3+D**3+C**3

def NumeroEspecial(N):
    if N>=100:
        NumeroEspecial(N-1)
        if EsNumeroEspecial(N):
            print (N)
NumeroEspecial(999)

