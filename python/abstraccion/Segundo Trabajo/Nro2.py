'''
En una lista se desea registrar los montos totales de las ventas diarias
 del mes de junio, de la empresa “Alfa''.Luego se desea determinar en
  cuántos días se tuvo montos superiores al promedio del mes.
'''

def RegistroVentasDiariasJunio():
    # numero de dias de junio
    n=30
    # lista de ventas
    Ventas=[]
    for i in range(0,n):
        v=int(input('ingrese venta del dia '+str(i+1)+':'))
        # agregar venta
        Ventas.append(v)

    # Promedio de ventas
    suma=0
    for v in Ventas:
        suma= v+suma
    # hallar el promedio
    promedio= suma/30

    # Dias mayores al promedio
    diasMayores=0
    for d in Ventas:
        if d > promedio:
            diasMayores+=1
    # numero de dias mayores al promedio
    return diasMayores

print(RegistroVentasDiariasJunio())


