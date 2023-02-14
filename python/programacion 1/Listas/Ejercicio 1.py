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
        Nota=int(input('Ingresar la nota'+str(k+1)+':'))
        Notas.append(Nota)
    return Notas

#-- MOSTRAR MENOR NOTA
def Menor(texto,lista):
    menor=21
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    print(texto,menor)

#CALCULAR LA MAYOR NOTA
def Mayor(texto,lista):
    mayor=-1
    for i in range(len(lista)):
        if mayor<lista[i]:
            mayor=lista[i]
    print(texto,mayor)

# modulo parar procesar aprobados
def ProcesarNotas(titulo,Notas,Mcondicion):
    print()
    print('PROCESO DE NOTAS '+titulo.upper())
    NotasP=[Nota for Nota in Notas if Mcondicion(Nota)]
    print('las notas son:',NotasP)
    print('El numeero de notas es:',len(NotasP))
    print('Promedio:', reduce(lambda x,y: x+y, NotasP)/len(NotasP))
    print('Nota mayor:',reduce(lambda x,y:x if x>y else y,NotasP))
    print('Nota menor:',reduce(lambda x,y:x if x<y else y,NotasP))

#     PROGRAMA PRINCIPAL
#-- Poner lista
print()
print('PROCESAR NOTAS')
#-- Leer el numero de alumnos
N=LeerNroEntero('Numero de alumnos:',1,100)
#-- leer las notas
Notas=LeerNotas(N)
#-- PRCESAR NOTAS
ProcesarNotas('Notas', Notas, lambda x: x>=0)
#-- PROCESAR APROBADOS
ProcesarNotas('aprobados', Notas, lambda x: x>=13.5)
#-- PROCESAR DESAPROBADOS
ProcesarNotas('desaprobados', Notas, lambda x: 9<x<=13.5)
#-- PROCESAR REPROBADOS
ProcesarNotas('reprobados', Notas, lambda x: x<=9)

