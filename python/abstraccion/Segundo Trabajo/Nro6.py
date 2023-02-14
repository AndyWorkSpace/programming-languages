'''
La biblioteca especializada de la Escuela Profesional de Ingeniería Informática
 y de sistemas en su afán de automatizar la atención a los estudiantes, solicitó
  un software para tal propósito. Uno de los integrantes del equipo implementó
   un módulo para leer en dos listas paralelas la relación de libros y el año 
   de su publicación. A Ud. Se le pide que escriba un módulo que determine el
    número de libros del último año.

'''
listalibro=["LibroA","LibroB","LibroC","LibroD","LibroE","LibroF"]
listaanio=[1940,1950,2001,2002,2012,2020,2020]
# Modulo numero de libros del ultimo anio
def LibrosUltimoAnio(Llibros,Lanios):
    # calcular el anio maximo
    anioMaximo=max(Lanios)
    cont=0
    for i in Lanios:
        # comparar anios
        if anioMaximo == i:
            # contar el numero de libros de ultimo anio
            cont=cont+1
    return cont 
        
print(LibrosUltimoAnio(listalibro,listaanio))
            