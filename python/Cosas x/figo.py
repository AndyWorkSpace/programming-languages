def figo(n):
    if (n==0 or n==1):
        return 1
    else:
        return figo(n-1)+figo(n-2)

n=int(input("ingrese numero="))
print(figo(n))
