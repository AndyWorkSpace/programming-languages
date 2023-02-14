# Modulo torre de Hanoi
def Hanoi(N,Inicio,Final):
    #---- Caso Base
    if N==1:
        print("Mover de",Inicio," a ",Final)
    #---- Caso Recurrente
    else:
        Auxiliar=6-Inicio-Final
        Hanoi(N-1,Inicio,Auxiliar)
        Hanoi(1,Inicio,Final)
        Hanoi(N-1,Auxiliar,Final)
    
#****************Progrma principal**********
#----- Leer Numero
N=int(input("Ingrese Nro. de discos = "))
# ---- Determinar los movimientos de los discos
Hanoi(N,1,3)
