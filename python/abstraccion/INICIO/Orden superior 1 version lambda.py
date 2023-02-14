def Funciones(Nombre):
    # Main del modulo funciones
    if (Nombre=="Suma"):
        return lambda X,Y: X+Y
    elif (Nombre=="Resta"):
        return lambda X,Y: X-Y
    elif (Nombre=="Multiplicacion"):
        return lambda X,Y: X*Y
    elif (Nombre=="Division"):
        return lambda X,Y: X/Y

#----- Main del programa o aplicacion
Funcion = Funciones("Suma")
print("Suma = ",Funcion(20,10))

x=Funciones("Multiplicacion")
print("Multiplicacion = ",x(10,3))
