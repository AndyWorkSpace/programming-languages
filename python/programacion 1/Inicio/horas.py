def LeerNroEntero(Texto, Minimo, Maximo = 100000000):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Numero fuera de rango...')
        Nro = int(input(Texto))
    return Nro

def Leer(texto):
    print(texto)
    H=leerNroEntero("ingrese hora=",0,23)
    M=leerNroEntero("ingrese minutos="),0,59)
    S=leerNroEntero("ingrese segundos="0,59)
    return(H,M,S)

def Segundos(HH,MM,SS):
    return(HH*3600+MM*60+SS)

def ConvertirSegundos(TotalSegundos):
    HH=TotalSegundos//3600
    MM=(TotalSegundos%3600)//60
    SS=(TotalSegundos%3600)%60
    return(HH,MM,SS)

#MODULO PRINCIPAL
H1,M2,S3=LeerTiempo("Ingrese primer tiempo=")


    
