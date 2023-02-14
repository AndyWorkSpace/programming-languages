# Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo selecciona algunos números
# en base a algún criterio
def Seleccionador(Modulo, *Numeros):
    for Elem in Numeros:
        if Modulo(Elem):
            print(Elem)
# *******************  PROGRAMA PRINCIPAL  **************************

# Mostrar los impares
print('Números Impares')
Seleccionador(lambda N: N%2 != 0 ,15,2,73,149,51,6,727,8,10)

# Mostrar los pares
print('Números pares')
Seleccionador(lambda N: N%2 == 0 ,15,2,73,149,51,6,727,8,10)

# Mostrar las números de dos dígitos
print('Números de dos dígitos')
Seleccionador(lambda N: 10 <= N <= 99 , 15,2,73,149,51,6,727,8,10)

# Mostrar ciudades que empiecen con C
print("Ciudades que empiezan con 'C'")
Seleccionador(lambda E : E>='C' and E<'D', 'Cusco', 'Ica', 'Puno', 'Cajamarca','Tacna')
