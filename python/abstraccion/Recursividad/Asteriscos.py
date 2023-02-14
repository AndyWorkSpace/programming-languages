'''
def Asteriscos(N):
    if N==1:
        print("0")
    else:
        Asteriscos(N-1)
        print("*")
'''
def Asteriscos(N):
    if N>0:
        Asteriscos(N-1)
        print('*')
    # El caso base está aca, pero se omite
Asteriscos(10)
