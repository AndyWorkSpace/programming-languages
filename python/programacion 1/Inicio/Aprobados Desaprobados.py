def Resultados(texto,*notas):
    Aprobados=0
    Desaprobados=0
    for i in notas:
        if i>=14:
            Aprobados=Aprobados+1
        else:
            Desaprobados=Desaprobados+1
    return(Aprobados,Desaprobados)

#Modulo principal

A,B=Resultados("Notas=",18,12,8,19,15,2,9,11,12,15)
print("El numero de aprobodados es=",A)
print("El numero de desaprobados es=",B)


            
