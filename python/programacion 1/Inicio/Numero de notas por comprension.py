# Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
from Libreria import *
#**** PROGRAMA principal ******
# Ponder titulo
print()
print('PROCESAR NOTAS')
#-- leer el numero de alumnos
N=LeerNroEntero('Numero de alumnos',0,20)
# -- leer la s notas
Notas=[]
for k in range(0,N):
    Notas.append(LeerNroReal('ingrese la nota'+str(k+1)+':',0,20))
# -- contar numero de alumnos aprobados
print('Aprobados:',len([x for x in Notas if x>13.5]))
# -- contar numero de alumnos desaprobados
print('Desaprobados:',len([x for x in Notas if 9<x<=13.5]))