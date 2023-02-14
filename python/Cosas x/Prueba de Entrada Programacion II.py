def Menor(arreglo):
    
    '''Calculamos el menor número para
       que sea eliminado'''
    
    menor=9999999999
    for i in range(4):
        if arreglo[i]<menor:
            menor=arreglo[i]
    arreglo.remove(menor)
    return arreglo

def Promedio(arreglo):

    '''Sacamos el promedio con las 3 notas
       más altas'''
    
    suma=0
    for i in range(3):
        suma=suma+arreglo[i]
    promedio=(suma/3)
    return promedio

#Módulo principal
arreglo=[]
print("INGRESE SUS CUATRO NOTAS")
for i in range(4):
    n=eval(input("nota="))
    while (n<0 or n>20):

        '''Verificamos los números'''

        n=eval(input("ingrese un número entre 0 y 20="))
    arreglo.append(n)
print("*Estas son las notas=",arreglo)
print("*Quitamos la menor nota=",Menor(arreglo))
print("*El promedio de las 3 notas más altas es=",Promedio(arreglo))
