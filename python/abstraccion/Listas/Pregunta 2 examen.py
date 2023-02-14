'''
def MesesConHeladas(T):
    for i in T:
        temp=0
        for j in range(0,len(T[i])):
            if T[i][j]<=0:
              temp+=1
        if temp>0:
            print(i,T[i])'''  

def MesesConHeladas(T):
    MH={}
    for k,v in T.items():
        if len([t for t in v if t<=0]) > 0:
            MH[k]=v
    return MH

def MesesConNroDiasHeladas(T):
    MH = MesesConHeladas(T)
    MDH={}
    for k,v in MH.items():
        MDH[k] = len([t for t in v if t<=0])
    return MDH
        
        
            # **************  PROGRAMA PRINCIPAL  *******************
# -- Crear diccionario de Temperaturas diarias
T = {}
# -- Ingresar temperaturas diarias mínimas de cada mes
T['ENE'] = [8,9,9,9,7,8,12,12,11,10,8,9,9,9,11,8,9,9,8,10,8,11,9,9,12,8,9,9,8,10,8]
T['FEB'] = [10,9,9,9,11,8,8,8,8,9,10,8,10,8,9,9,12,7,8,10,9,8,10,8,11,9,9,7]
T['MAR'] = [10,10,10,9,7,8,9,6,8,10,8,6,9,9,7,8,9,9,8,10,8,11,9,9,7,8,8,8,9,10,8]

T['ABR'] = [9,8,7,7,7,8,9,9,9,7,8,10,10,9,10,8,11,9,9,11,8,9,5,8,7,7,6,7,7,6]
T['MAY'] = [6,5,7,5,3,4,2,1,2,3,2,1,3,3,-1,-2,2,2,1,2,1,0,-1,-1,-2,0,1,-1,2,-1,1]
T['JUN'] = [5,3,4,2,-1,-2,-1,1,2,3,-2,1,3,3,-1,-4,4,-2,-1,2,1,0,1,1,-2,0,1,-1,2,1]

T['JUL'] = [2,2,1,2,1,0,-1,-1,-2,0,1,-1,2,-1,1,3,2,1,3,3,-1,-2,4,2,1,2,3,5,3,4,3]
T['AGO'] = [4,-1,2,-1,3,4,2,7,2,3,2,7,3,6,5,7,5,3,4,2,6,5,3,2,5,6,7,7,7,6,8]
T['SET'] = [6,5,7,5,5,5,8,7,4,5,6,7,6,6,5,7,5,6,7,6,6,7,8,8,8,9,7,7,10,9]

T['OCT'] = [7,9,7,9,7,8,6,10,11,10,8,9,9,9,9,8,9,9,8,10,8,7,9,9,7,8,9,9,8,10,8]
T['NOV'] = [7,8,10,9,8,10,8,11,9,9,7,9,9,9,11,8,8,8,8,9,10,8,10,8,9,9,12,11,11,12]
T['DIC'] = [10,10,10,9,7,8,9,12,8,10,8,12,9,9,7,8,9,9,8,10,8,11,9,9,7,8,8,8,9,10,8]

# -- Módulo para determinar los meses en que hubo heladas
MH = MesesConHeladas(T)
for k,v in MH.items():
    print(k,v)

MDH = MesesConNroDiasHeladas(T)
for k,v in MDH.items():
    print(k,v)
