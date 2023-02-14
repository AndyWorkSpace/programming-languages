#USO DEL LAMBDA

cubos=lambda n:pow(n,3)
print(cubos(13))

#cubos=lambda numero=numero**3
#print(cubos(13))

#USANDO LAMBDA Y FORMAT

destacarValor=lambda comision:"¡{}!$" .format(comision)
comisionAna=15585

print(destacarValor(comisionAna))

#USO DEL FORMAT

nombre=input(str("ingrese nombre="))
edad=int(input("ingrese edad="))

print("tu nombre es {0} y tienes {1}".format(nombre,edad))
