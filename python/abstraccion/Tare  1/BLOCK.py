# Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# en base a algún criterio

def Seleccionador(Modulo,*Numeros):
    for Elem in Numeros:
        if Modulo(Elem):
            print(Elem)
#---------------MODULOS------------------#
def Sumadigitos(Elem):
    m,n,p = Elem//100,((Elem%100)//10),(Elem%100)%10
    if Elem == (m**3)+(n**3)+(p**3):
        return Elem

#____________Modulo principal__________

print('Numeros que la suma de digitos al cubo')
Seleccionador(Sumadigitos,149,23,51,4,743,727,370)

