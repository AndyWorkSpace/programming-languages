class Coche():
    chasis=250
    ancho = 12
    ruedas=4
    enmarcha= False

    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if self.enmarcha==True:
            return ("el conche enmarcha")
        else:
            return ("quieto")
        

miCoche=Coche()
print("el chasis es=",miCoche.chasis)
miCoche.arrancar() #SIRVE PARA ARRANCAR EL COCHE
print("Esta=",miCoche.estado())

print("**********creamos el segundo objeto**************")

micoche2=Coche()
print("chasis=",micoche2.chasis)
print("Esta=",micoche2.estado())
