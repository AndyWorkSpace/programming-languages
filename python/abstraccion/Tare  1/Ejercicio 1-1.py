# Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# en base a algún criterio
def Seleccionador(Modulo,*Numeros):
    for Elem in Numeros:
        if Modulo(Elem):
            print(Elem)

# Modulo determinar si es primo
def Primo(num):
    if num < 2:     
        return False
    for i in range(2, num):
        if num % i == 0:    
            return False
    return True

# *******************  PROGRAMA PRINCIPAL  **************************

# Mostrar los primos
print('Números Primos')
Seleccionador(Primo,15,2,73,1,149,51,6,727,8,10)
