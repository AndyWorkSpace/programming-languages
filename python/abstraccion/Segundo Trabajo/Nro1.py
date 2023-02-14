# Modulo nombre distintos
def NombresDiferents(Lista):
    # lista de nombres diferentes
    listaNombres=[]
    # Busqueda de nombres iguales en la lista
    for i in Lista:
        if i.upper() not in listaNombres:
            # agregar nombres nuevos
            listaNombres.append(i.upper())
    return len(listaNombres)

# *********** programa principal ************
#- lista de nombres RENIEC
ListaReniec=['alvaro','elias','Vanessa','ruth','vanessa','angie','sol']
#- mostrar nombres distintos
print('Hay {} nombre distintos en la lista'.format(NombresDiferents(ListaReniec)))