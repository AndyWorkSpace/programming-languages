# Programa de tablas aritmeticas
from Libreria import *
# ************************ MÓDULOS **************************
# Tabular
def Tabular(N,F):
    print("***TABULAR FUNCION***")
    print("x\tF(x)")
    for x in range(1,N+1):
        print(x,"\t",F(x))

# *****PROGRAMA PRINCIPAL***** #

#LEER EL VALOR DE N
N=LeerNroEntero("ingrese un numero= ",1)
# TABULAR LA FUNCION F
Tabular(N,lambda x:3*x**2 + 5*x + 1)
# TABULAR LA FUNCION G
Tabular(N,lambda x:x**3 + 2*x**2 - 2)
# TABULAR LA FUNCION H
Tabular(N,lambda x:(x**2 - 9)/0.5)
