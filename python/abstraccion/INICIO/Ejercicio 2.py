#Modulo Suma
def Suma(X,Y):
    return(X+Y)

#Modulo Mayor
def Mayor(X,Y):
    return(X if X>Y else Y)

#Moudlo MCD
def MCD(A,B):
    R=A%B
    while R!=0:
        A=B
        B=R
        R=A%B
    return(B)

# Modulo procesar
def Procesar(Modulo,*Nros):
    R=None
    for Nro in Nros:
        R=Nro if R==None else Modulo(R,Nro)
    return R
    

#*************MODULO PRINCIPAL**********#
S=Procesar(Suma,24,96,120,30,36,72)
print("Suma = ",S)
M=Procesar(Mayor,24,96,120,30,36,72)
print("Mayor = ",M)
mcd=Procesar(MCD,24,96,120,30,36,72)
print("MCD = ",mcd)


