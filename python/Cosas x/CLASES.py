class Coche():
    chasis=250
    ancho = 12
    ruedas=4
    enmarcha= False

    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if self.enmarcha==True:
            return ("el conches enmarcha")
        else:
            return ("quieto")
        

miCoche=Coche()

print("el chasis es=",miCoche.chasis)
print("ancho del coche=",miCoche.ancho)

miCoche.arrancar() #SIRVE PARA ARRANCAR EL COCHE
print("Esta=",miCoche.estado())

