#  LEER NUMEROS
def LeerNumeros(texto):
    A = eval(input(texto+"  numerador  = "))
    B = eval(input(texto+" denominador = "))
    while B==0:
        print("Ingrese un numero diferente de 0")
        B = eval(input(texto+" denominador="))
    return(A,B)

#  MCD
def MCD(A,B):
    R=A%B
    while (R!=0):
        A=B
        B=R
        R=A%B
    return(B)

#  SIMPLIFICAR
def Simplificar(A,B):
    M=MCD(A,B)
    A=A//M
    B=B//M
    return(A,B)

# Menu de operaciones
def Menu():
    print()
    print(' ***** OPERACIONES *****')
    print('Sumar       -- opcion 1')
    print('Restar      -- opcion 2')
    print('Multiplicar -- opcion 3')
    print('Dividir     -- opcion 4')
    
#*******SUMA
def Sumar(N1,D1,N2,D2):
     NS=N1*D2+N2*D1
     DS=D1*D2
     NS,DS=Simplificar(NS,DS)
     return(NS,DS)
    
#*******RESTA
def Restar(N1,D1,N2,D2):
    NS=N1*D2-N2*D1
    DS=D1*D2
    NS,DS=Simplificar(NS,DS)
    return(NS,DS)

#******MULTIPLICAR
def Multiplicar(N1,D1,N2,D2):
    NS=N1*N2
    DS=D1*D2
    NS,DS=Simplificar(NS,DS)
    return(NS,DS)

#******DIVISION
def Dividir(N1,D1,N2,D2):
    NS=N1*D2
    DS=N2*D1
    NS,DS=Simplificar(NS,DS)
    return(NS,DS)

# MODULO PORCESAR NRO RACIONALES
def Procesar(ModuloProcesar):
    #**Leer dos numeros racionales
    N1,D1=LeerNumeros("Primer")
    N2,D2=LeerNumeros("Segundo")
    NS,DS=ModuloProcesar(N1,D1,N2,D2)
    #**Mostrar resultado
    print("Resultado=",NS,"/",DS)

#   MENU
def ProcesarNrosRacionales():
    opcion=0
    while opcion !=5:
    #Mostrar menu
        Menu()
        opcion=int(input("ingrese opcion = "))
        if   opcion==1:
            Procesar(Suma)
        elif opcion == 2:
            Procesar(Restar)
        elif opcion == 3:
            Procesar(Multiplicar)
        elif opcion == 4:
            Procesar(Dividir)
##########################
#         PROGRAMA PRINCIPAL
############################
ProcesarNrosRacionales()
