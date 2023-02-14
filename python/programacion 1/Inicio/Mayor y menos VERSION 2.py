def LeerNota(Texto, Minimo, Maximo = 100000000):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Numero fuera de rango...')
        Nro = int(input(Texto))
    return(Nro)

#CALCULAR LA MENOR NOTA
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
    
#*************MODULO PRINCIPAL**********#
#CREAR LISTA
n=LeerNota("Ingrese le numero de notas=",0)
lista=[]
for i in range(0,n):
    p=LeerNota("Ingrese Nota=",0,20)
    lista.append(p)
print(lista)

#CALCULAR MAYOR Y MENOR
Menor("La menor nota es=",lista)
Mayor("La mayor nota es=",lista)


            
