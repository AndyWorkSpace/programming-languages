# Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# en base a algún criterio
def Seleccionador(S, *Numeros):
    for Nro in Numeros:
        if S(Nro):
            print(Nro)

# *******************  MÓDULOS DE LA APLICACIÓN  ********************

# Módulo para determinar si un número es impar
def EsImpar(N):
    return N % 2 != 0

# Módulo para determinar si un número es par
def EsPar(N):
    return N % 2 == 0;

# Módulo para mostrar los números de dos dígitos
def EsNroDeDosDigitos(N):
    return 10 <= N <= 99


# *******************  PROGRAMA PRINCIPAL  **************************

# Mostrar los impares
print('Números Impares')
Seleccionador(EsImpar, 15,2,73,149,51,6,727,8,10)

# Mostrar los pares
print('Números pares')
Seleccionador(EsPar, 15,2,73,149,51,6,727,8,10)

# Mostrar las números de dos dígitos
print('Números de dos dígitos')
Seleccionador(EsNroDeDosDigitos, 15,2,73,149,51,6,727,8,10)
