import math
unidades = ["cero", "uno", "dos" ,"tres" ,"cuatro" ,"cinco" ,
            "seis" ,"siete" ,"ocho" ,"nueve","diez"]
especiales = ["once", "doce","trece","catorce", "quince",
              "diezciseis", "diecisiete", "dieciocho", "diecinueve"]
decenas = ["veinte", "treinta","cuarenta","cincuenta", "sesenta",
           "setenta", "ochenta", "noventa"]

#El dato ingresado lo convierte a entero y lo almacena en la variable num
num = int(input("Ingrese un numero entre 0-99: "))

if (num >=0 and num <11):
    print (unidades[num])

elif (num < 20):
    print (especiales[num-11])

elif (num <100):
    
    unid = num% 10;
    #math.floor -> obtiene la parte entera de la division num/10
    #luego ese resultado lo convertimos a entero, 
    dec = int(math.floor(num/10))
    if (unid == 0):
        print (decenas[dec-2]) 
    else:
        print (decenas[dec-2], "y" , unidades[unid])
else:
    print ("El numero debe ser menor a 100")
