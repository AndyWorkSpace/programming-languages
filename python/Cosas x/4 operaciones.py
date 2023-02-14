def suma(a,b):
    return(a+b)

def resta(a,b):
    return(a-b)

def mult(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

print("****Elija la operacion****")
print("suma=1, resta=2 \
       multiplicar=3, dividir=4")
n=int(input("ingrese su operacion="))
while (n<=1 and n>=4):
    n=int(input("ingrese un numero entre 1 y 4="))
    
a=eval(input("ingrese un primer numero="))
b=eval(input("ingrese un segundo numero="))
          
if   (n==1):
    print("la suma es=",suma(a,b))
elif (n==2):
    print("la resta es=",resta(a,b))
elif (n==3):
    print("la multiplicacion es=",mult(a,b))
elif (n==4):
    print("La division es=",div(a,b))
