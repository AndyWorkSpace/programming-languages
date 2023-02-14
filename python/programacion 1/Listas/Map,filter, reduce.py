from functools import *

#***** PROGRAMA PRINCIPAL ****#
# gererar una lista
lista=[1,2,3,4,5,6,7,8,9,10]   
print()
print('lista original')
print(lista)

# Mapear(procesar)cada elemento dela lista para elevarlo al cuadrado
print()
print('Elementos de la lista elevado al cuadrado')
L01=[E**2 for E in lista]
#L01=map(lambda x:x**2,lista)
print(list(L01))

# Filtrar los elementos que cumplen una determinada caracteristica
print()
#L02=filter(lambda x: x%2!=0,lista)
print('Numeros impares de una lista')
L02=[E for E in lista if E%2==1]
print(list(L02))

# Reducir una lista a un unico elemento
print()
L03=reduce(lambda x,y:x+y,lista)
print('Suma de elementos de una lista')
print("suma de elementos: ",L03)