# Programa de tablas aritmeticas
from Libreria import *
# ************************ MÓDULOS **************************
# Funcion 1
def F(x):
    return(3*x**2 + 5*x + 1)

# Funcion 2
def G(x):
    return x**3 + 2*x**2 - 2

# Funcion 3
def  H(x):
    return (x**2 - 9)/0.5

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
Tabular(N,F)
# TABULAR LA FUNCION G
Tabular(N,G)
# TABULAR LA FUNCION H
Tabular(N,H)
