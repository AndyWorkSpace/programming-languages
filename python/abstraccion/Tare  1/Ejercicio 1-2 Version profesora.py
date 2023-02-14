# Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números

def Seleccionador(Modulo,*Numeros):
    for Elem in Numeros:
        if Elem==Modulo(Elem):
                print (Elem)
            
def Sumadigitos(Elem):
    Suma=0
    while Elem>0:
        Suma=Suma+(Elem%10)**3
        Elem=Elem//10
    return Suma
        
#____________Modulo principal__________

print('Suma de digitos al cubo igual al número')
Seleccionador(Sumadigitos,149,23,51,4,743,727,370)

