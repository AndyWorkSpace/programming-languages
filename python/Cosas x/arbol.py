def Copa():
    for k in range(1,20,2):
        Espacios=(20-k)//2
        print(' '*Espacios +'*'*k)

def Tronco():
    for k in range(1,6):
        print(' '*9+'*'*3)

def Piso():
    print(' '+'*'*16)

#Modulo principal
Copa()
Tronco()
Piso()
