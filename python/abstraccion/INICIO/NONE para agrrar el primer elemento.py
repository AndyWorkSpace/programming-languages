# Programa para procesar números
# Módulo MCD
def MCD(A, B):
    R = A % B
    while R  != 0:
        A = B
        B = R
        R = A % B
    return B

# Módulo Procesar
def Procesar(Modulo, *Nros):
    R = None
    for Nro in Nros:
        R = Nro if R == None else Modulo(R,Nro)
    return R

# Módulo principal
S = Procesar(lambda A, B : A + B, 24, 96, 120, 30, 36, 72)
print('Suma = ', S)

M = Procesar(lambda X, Y : X if X > Y else Y, 24, 96, 120, 30, 36, 72)
print('Mayor', M)

mcd = Procesar(MCD, 24, 96, 120, 30, 36, 72)
print('MCD', mcd)

Prom = Procesar(lambda A, B : A + B, 24, 96, 120, 30, 36, 72)/6
