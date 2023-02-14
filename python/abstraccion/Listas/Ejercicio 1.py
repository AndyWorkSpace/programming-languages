from functools import *

LNotas=[10,12,16,20,20,18,8,16,14,20,6,16,12,14,10,8,20]
print('Notas:',LNotas)

# Notas desaprobadas
LDes=[E for E in LNotas if E<9]
print('Notas desaprobadas:',LDes)

# Promedio de notas
Suma=reduce(lambda x,y: x+y,LNotas)
Promedio=Suma/len(LNotas)
print('Promedio de notas:',Promedio)

# notas encima del promedio
NotaEncima=[E for E in LNotas if E>=Promedio]
print('Notas mayor al promedio:',NotaEncima)
