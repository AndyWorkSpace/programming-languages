#Validar coordenada
def LeerNroEntero(Texto, Minimo, Maximo = 100000000):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Numero fuera de rango...')
        Nro = int(input(Texto))
    return Nro

#Calcular distancia
def distancia(a,b):
    n=(((a**2)+(b**2))**(1/2))
    return(n)


#*************PROGRAMA PRINCIPAL**********
# LEER NUMERO DE COORDENADAS
n=int(input("ingrese el numero de coordenadas="))
maxi=0
for i in range(n):
    a=eval(input("ingrese x="))
    b=eval(input("ingrese y="))
    print("coordenada=","[",a,",",b,"]")
    print("distancia=",distancia(a,b))
    if maxi<=distancia(a,b):
        maxi=distancia(a,b)
print("la distancia maxima al origen de coordenadas es=",maxi)

