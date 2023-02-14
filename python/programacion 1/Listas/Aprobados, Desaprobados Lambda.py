from Libreria import *
from functools import *

# MODULOS
#-- modulo leer las notas
def LeerNotas(N):
    Notas=[]
    #-- Poner titulo
    print()
    print('Ingresar las notas')
    for k in range (0,N):
        Nota=LeerNroReal('Ingresar la nota'+str(k+1)+':',0,20)
        Notas.append(Nota)
    return Notas

# modulo parar procesar aprobados
def ProcesarNotas(titulo,Notas,Mcondicion):
    print()
    print('PROCESO DE NOTAS '+titulo.upper())
    NotasP=[Nota for Nota in Notas if Mcondicion(Nota)]
    print('las notas son:',NotasP)
    print('El numeero de notas es:',len(NotasP))
    print('Promedio:', reduce(lambda x,y: x+y, NotasP)/len(NotasP))

#     PROGRAMA PRINCIPAL
#-- Poner lista
print()
print('PROCESAR NOTAS')
#-- Leer el numero de alumnos
N=LeerNroEntero('Numero de alumnos:',1,100)
#-- leer las notas
Notas=LeerNotas(N)
#-- PROCESAR APROBADOS
ProcesarNotas('aprobados', Notas, lambda x: x>=13.5)
#-- PROCESAR DESAPROBADOS
ProcesarNotas('desaprobados', Notas, lambda x: 9<x<=13.5)
#-- PROCESAR REPROBADOS
ProcesarNotas('reprobados', Notas, lambda x: x<=9)

