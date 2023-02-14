lista=[] #metodo tradicional
for i in range(1,10):
    if i%2==0:
        lista.append(i)

print(lista)
         #metodo usando listas de comprension
lista=[numero for numero in range(1,10) if numero%2==0]
print (lista)
#----------------------------
#segundo ejemplo
lista2=[]  #metodo tradicional
for i in range(1,10):
    lista2.append(i**2)

pares=[]
for i in lista2:  #no afecta en nada usar 2 veces i en diferenres funciones
    if (i%2==0):   #range(len(lista2)== lista2?
        pares.append(i)
print(pares)
    
           #Metodo listas de comprension
lista=[numero for numero in
           [numero**2 for numero in range(1,10)]
               if numero%2==0]
print (lista)
#----------------------------


