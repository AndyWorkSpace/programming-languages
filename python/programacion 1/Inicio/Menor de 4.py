#Leer las tres notas
def LeerEntero(texto,Min=0,Max=20):
    n=int(input(texto))
    while n<Min or n>Max:
        print("ERROR,fuera de rango")
        n=int(input("Vuelva a "+texto))
    return(n)

#LEER NOTAS
def LeerNotas(Min=0,Max=20):
    N1=LeerEntero("Ingrese nota1=",Min,Max)
    N2=LeerEntero("Ingrese nota2=",Min,Max)
    N3=LeerEntero("Ingrese nota3=",Min,Max)
    N4=LeerEntero("Ingrese nota3=",Min,Max)
    return(N1,N2,N3,N4)

#CALCULAR MENOR
def MenorDos(A,B):
    return(A if A<B else B)

def MenorDeCuatro(A,B,C,D):
    return(MenorDos(A,B) if MenorDos(A,B)<MenorDos(C,D) else MenorDos(C,D))


#CALCULAR PROMEDIO
def CalcularPromedio(N1,N2,N3,N4):
    M=MenorDos(MenorDos(N1,N2),MenorDos(N3,N4))
    Promedio=(N1+N2+N3+N4-M)/3
    return(Promedio)
    
#Leer la tres notas
Nota1,Nota2,Nota3,Nota4=LeerNotas(0,100)

#Calcular promedio
print(CalcularPromedio(Nota1,Nota2,Nota3,Nota4))
