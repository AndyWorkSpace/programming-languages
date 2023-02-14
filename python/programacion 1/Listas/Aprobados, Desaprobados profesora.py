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
def ProcesarAprobados(Notas):
    print()
    print('PROCESO DE NOTAS APROBADAS')
    NotasA=[Nota for Nota in Notas if Nota >=13.5]
    print('las notas son:',NotasA)
    print('El numeero de notas es:',len(NotasA))
    print('Promedio:', reduce(lambda x,y: x+y, NotasA)/len(NotasA))

# Modulo para procesar desaprobados
def ProcesarDesaprobados(Notas):
    print()
    print('PROCESO DE NOTAS DESAPROBADAS')
    NotasD=[Nota for Nota in Notas if 9<Nota<=13.5]
    print('las notas son:',NotasD)
    print('El numeero de notas es:',len(NotasD))
    print('Promedio:', reduce(lambda x,y: x+y, NotasD)/len(NotasD))

#     PROGRAMA PRINCIPAL
#-- Poner lista
print()
print('PROCESAR NOTAS')
#-- Leer el numero de alumnos
N=LeerNroEntero('Numero de Notas:',1,100)
#-- leer las notas
Notas=LeerNotas(N)
#-- PROCESAR APROBADOS
ProcesarAprobados(Notas)
#-- PROCESAR DESAPROBADOS
ProcesarDesaprobados(Notas)