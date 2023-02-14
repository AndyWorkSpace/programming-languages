## Programa para Seleccionar números
# ************************  MÓDULO PATRÓN  **************************
# Dado un conjunto de números, este módulo convierte algunos números
# Modulo Convertir
def Convertidor(S,C,*Numeros):
    print("Numero Invertido")
    for Nro in Numeros:
        M=0
        while Nro>0:
            M=S(M,Nro)
            Nro=C(Nro)
        print(M)

# *******************  PROGRAMA PRINCIPAL  **************************
# Numero de digitos
print('Números y sus Números de digitos')
Convertidor((lambda M,Nro:M*10 + Nro%10),(lambda Nro:Nro//10)
            ,12,232,3,4,45,687)

