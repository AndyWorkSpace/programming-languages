# Modulo para determinar el multiplos de tres
# de un numero
# Número espacial es aquel que es igual a la suma del cubo de sus Digitos

'''
def MultiploTres(N):
    if N == 0:
        return 0
    else:
        if N % 3 == 0:
            return 1 + MultiploTres(N-1)
        else:
            return 0 + MultiploTres(N-1)

'''
'''
def MultiploTres(N):
    if N == 0:
        return 0
    else:
        # return (N % 3==0? 1:0) + MultiplosTres(N-1)
        return (1 if N % 3==0 else 0 ) + MultiplosTres(N-1)
'''
'''
def MultiploTres(N):
    return 0 if (N==0) else (1 if N % 3==0 else 0 ) + MultiploTres(N-1)
'''

def MultiploTres(N):
    return 0 if (N==0) else  (N % 3==0  + MultiploTres(N-1))
    # El true o false cuando está fuera del if o while se representan
    # como : TRUE=1 y False=0 cuando está junto a operaciones matematicas

print("Multplos de 3: ",MultiploTres(15))
