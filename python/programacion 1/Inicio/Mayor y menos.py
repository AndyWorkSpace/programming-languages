def LeerNota(Texto, Minimo, Maximo):
    Nro = int(input(Texto))
    while(Nro < Minimo or Nro > Maximo):
        print('Error. Numero fuera de rango...')
        Nro = int(input(Texto))
    return(Nro)

def Menor(texto,lista): # *lista = 2,34,6,8,0,43
    menor=21
    for num in range(len(lista)):
        if num<menor:
            menor=num
    print(texto,menor)

def Mayor(texto,lista):
    mayor=-1
    for num in lista:
        if mayor<num:
            mayor=num
    print(texto,mayor)
    
#*************MODULO PRINCIPAL**********#
    
n=LeerNota("Ingrese le numero de notas=",0,100)
lista=(""*n)
for i in range(0,n):
    p=LeerNota("Ingrese Nota=",0,20)
    lista.insert(i,p)
print(lista)

Menor("La menor nota es=",lista)
Mayor("La mayor nota es=",lista)


            
