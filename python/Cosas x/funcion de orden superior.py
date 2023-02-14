def seleccion(operacion):
    def suma(n,m):
        return(n+m)
    def multiplicacion(n,m):
        return(n*m)

    if operacion=="suma":
        return suma
    elif operacion=="multi":
        return multiplicacion

fguardada = seleccion("multi")
print(fguardada(12,13))
