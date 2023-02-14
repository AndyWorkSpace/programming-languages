def Funciones(Nombre):
    def Suma(X,Y):
        return X+Y
    def Resta(X,Y):
        return X-Y
    def Multiplicacion(X,Y):
        return X*Y
    def Division(X,Y):
        return X/Y

    # Main del modulo funciones
    if (Nombre=="Suma"):
        return Suma
    elif (Nombre=="Resta"):
        return Resta
    elif (Nombre=="Multiplicacion"):
        return Multiplicacion
    elif (Nombre=="Division"):
        return Division

#----- Main del programa o aplicacion
Funcion = Funciones("Suma")
print("Suma = ",Funcion(20,10))
x=Funciones("Multiplicacion")
print("Multiplicacion = ",x(10,3))
