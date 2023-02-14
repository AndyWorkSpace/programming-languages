import random
# Modulo para leer un número
def LeerNroEntero(Texto, Minimo, Maximo = 100000000):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Número fuera de rango...')
        Nro = int(input(Texto))
    return Nro

# Modulo Juego del Resto
def Juego(n):
	while n>1:
		# Elegir número de galleros por el usuario
		m=LeerNroEntero("---->Elige el número de galletas: ",1,3)
		n=n-m
		# Dejar de jugar cuando el usuario se quede con las ultimas galletas
		if n<=0:
			break
		# Mostrar las que quedan
		print("Quedan ",n," galletas")
		# Elegir número de galletas por la computadora
		Computadora=random.randint(1,3)
		print("-->Computadora: Mi turno de elegir: ",Computadora)
		n=n-Computadora
		# Mostrar las que quedan luego que eliga la computadora
		print("Quedan ",n," galletas")
		# Modificar el numero de galletas cuando la computadora eliga
		# las galleras restantes y sea igual a 0
		if n==0:
			return n-1
	return n

# Modulo Mostrar Resultado
def Queda(n):
	if Juego(n)>=0:
		return "*** HAS PERDIDO ***"
	else:
		return "*** FELICITACIONES, HAS GANADO ***"

#********************* Programa Principal *****************#
#Leer numero de galletas
n=LeerNroEntero("Ingrese el número de galletas en el Juego: ",1)
# Mostrar resultado
print(Queda(n))

