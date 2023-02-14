def divide():

    try:
        op1=eval(input("ingrese valor:"))
        op2=eval(input("ingrese valor:"))
        print("la divison es " + str(op1/op2))
    except ValueError:
        print("Valores incorrectos")
    except ZeroDivisionError:
        print("No se puede dividir entre zero")
    finally:
        print("FINALIZADO")
divide()
print("FINALIZADO")
