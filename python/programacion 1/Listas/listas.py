from functools import *

#***** PROGRAMA PRINCIPAL ****#
# gererar una lista
lista=[1,2,3,4,5,6,7,8,9,10]   
print()
print('lista original')
print(lista)
# Mapear(procesar)cada elemento dela lista para elevarlo al cuadrado
print('lista mapeada')
L01=map(lambda x:x**2,lista)
print(list(L01))
# Filtrar los elementos que cumplen una determinada caracteristica
L02=filter(lambda x: x%2!=0,lista)
print('Numeros impares de una lista')
print(list(L02))
# Reducir una lista a un unico elemento
L03=reduce(lambda x,y:x+y,lista)
print('lista reducida')
print("suma de elementos: ",L03)