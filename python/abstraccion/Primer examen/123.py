#          MÓDULOS                  #
# Seleccionar un NÚmero
def CogerNumeros(*Numeros):
    for N in Numeros:
        if RepiteNum(N):
            print("Se repiten :",RepiteNum(N),':numeros en:',N)
            
# MÓdulo analizar si se repite
def RepiteNum(N):
    Repite=0
    while N>10:
        #--Agarrar última cifra
        y=N%10
        #--Asigar un valor a N
        z=N
        #--Comparar la última cifra con la última cifra actualizada
        for y in range(1,len(str(N))):
            #--Comparar
            if y==(z//10)%10:
                Repite=Repite+1
            #-- Actualizar Z
            z=z//10
        #--Devolver el número de veces que se repite
        return Repite
        #--Actualizar N
        N=N//10

#************** PROGRAMA PRINCIPAL *********#
print('11,123,1222,12345,1456711')
# Mostrar si algún número se repite dentro de un número
CogerNumeros(11,123,1222,12345,1456711)
