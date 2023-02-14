# Modulo Recursivo para calcular la division entera
'''
def InvertirT(Texto):
    #----- CASO BASE
    if Texto=="":
        return ""
    #----- CASO RECURRENTE
    else:
        return InvertirT(Texto[1:])+Texto[0]
'''
def InvertirT(Texto):
    #--- CASO BASE Y RECURRENTE
    return '' if Texto=='' else (InvertirT(Texto[1:])+Texto[0])
#************+*PROGRAMA PRINCIPAL********
# LEER TEXTO
Texto=str(input("Ingrese un texto: "))
#Mostrar texto invertido
print("texto invertirdo: ",InvertirT(Texto))
