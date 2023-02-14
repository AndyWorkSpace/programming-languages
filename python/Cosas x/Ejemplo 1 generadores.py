#primera forma
def generaPares(limite):
    num=1
    Lista=[]
    while num<limite:
        Lista.append(num*2)
        num=num+1
    return(Lista)
print(generaPares(10))

#######################

#segunda forma
def generaPares(limite):
    num=1
    while num<limite:
        yield(num*2)
        num=num+1
devuelvePares=generaPares(10)
for i in devuelvePares:
    print(i)
#USANDO LA FUNCION NEXT
    
