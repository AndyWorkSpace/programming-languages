from Libreria import *
#**********Modulo*****************
def Factorial(N):
    #-------- CASO BASE
    if N==0:
        return 1
    #-------- CASO RECURRENTE
    else:
        return N*Factorial(N-1)
    
#**************  Programa principal*****************

print("Factorial =",Factorial(5))
