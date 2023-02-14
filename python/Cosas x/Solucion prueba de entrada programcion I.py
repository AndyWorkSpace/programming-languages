def NroEntero(Texto, Min, Max = 1000000):
    Nro = int(input(Texto))
    while(Nro < Min) or (Nro > Max):
        print('Numero fuera de rango')
        Nro = int(input(Texto))
    return Nro

# ---- Modulo Menor de dos números
def MenorDos(N1,N2):
    # Determinar el mneor de dos números
    return N1 if N1 < N2 else N2

# ---- Modulo Nota Menor
def NotaMenor(N1, N2, N3, N4):
    # Determinar la nota menor
    return MenorDos(MenorDos(N1, N2), MenorDos(N3, N4))


# ----- Modulo Principal
# Leer las Notas validando
N1 = NroEntero('Ingresa Nota 1: ',0,20)
N2 = NroEntero('Ingresa Nota 2: ',0,20)
N3 = NroEntero('Ingresa Nota 3: ',0,20)
N4 = NroEntero('Ingresa Nota 4: ',0,20)
# Determinar Menor
Menor = NotaMenor(N1,N2,N3,N4)
# Calcular Promedio
Promedio = (N1+N2+N3+N4-Menor)/3
# Mostrar Promedio
print('Nota menor = ',Menor)
print('Promedio = ',Promedio)
