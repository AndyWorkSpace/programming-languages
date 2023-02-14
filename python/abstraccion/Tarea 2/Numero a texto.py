from Libreria import *

# Modulo descomponer
def Descomponer(N):
    c=N//100
    d=(N%100)//10
    u=N%10
    return c,d,u
# Modulo lectura
def Lectura(N):
    # lectura unidades
    def unidades(N):
        c,d,u=Descomponer(N)
        if u==0:
            return " "
        elif u==1:
            return 'UNO'
        elif u==2:
            return "DOS"
        elif u==3:
            return "TRES"
        elif u==4:
            return "CUATRO"
        elif u==5:
            return "CINCO"
        elif u==6:
            return "SEIS"
        elif u==7:
            return "SIETE"
        elif u==8:
            return "OCHO"
        elif u==9:
            return "NUEVE"
    # lectura descenas  
    def decenas(N):
        c,d,u=Descomponer(N)
        if d==0:
            return ""
        elif d==1:
            if u==0:
                return "DIEZ" 
            elif u==1:
                return "ONCE"
            elif u==2:
                return "DOCE"
            elif u==3:
                return "TRECE"
            elif u==4:
                return "CATORCE"
            elif u==5:
                return "QUINCE"
            else:
                return "DIECI"
        elif d==2:
            if u==0:
                return 'VEINTE'
            else:
                return 'VEINTI'
        elif d==3:
            if u==0:
                return 'TREINTA'
            else:
                return 'TREINTA Y'
        elif d==4:
            if u==0:
                return 'CUARENTA'
            else:
                return 'CUARENTA Y '
        elif d==5:
            if u==0:
                return 'CINCUENTA'
            else:
                return 'CINCUENTA Y'
        elif d==6:
            if u==0:
                return 'SESENTA'
            else:
                return 'SESENTA Y '
        elif d==7:
            if u==0:
                return 'SETENTA'
            else:
                return 'SETENTA Y '
        elif d==8:
            if u==0:
                return 'OCHENTA'
            else:
                return 'OCHENTA Y '
        elif d==9:
            if u==0:
                return 'NOVENTA'
            else:
                return 'NOVENTA Y '
    # lectura centenas
    def centenas(N):
        c,d,u=Descomponer(N)
        if c==1:
            if d==0 and u==0:
                return 'CIEN'
            else:
                return 'CIENTO'
        elif c==2:
            return 'DOSCIENTOS'
        elif c==3:
            return 'TRESCIENTOS'
        elif c==4:
            return 'CUATROCIENTOS'
        elif c==5:
            return 'QUINIENTOS'
        elif c==6:
            return 'SEISCIENTOS'
        elif c==7:
            return 'SETECIENTOS'
        elif c==8:
            return 'OCOHOCIENTOS'
        elif c==9:
            return 'NOVECIENTOS'    
    return centenas(N)+decenas(N)+unidades(N)
#******************* PROGRAMA PRINCIPAL***********"
# Mostrar lectura del numero
print('INGRESE UN NUMERO DE 3 DIGITOS')
N=LeerNroEntero('Ingrese un número: ',1)
print(Lectura(N))

