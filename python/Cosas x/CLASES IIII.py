class Coche():
    
    def __init__(self): #estado inicial          
        self.chasis=250
        self.ancho = 12
        self.__ruedas=4 #la variable ruedas no sea accesible a cambios fuera de la clase
        self.enmarcha= False
        

    def arrancar(self,arrancamos): #El seld se considera como un parametro nulo
        self.enmarcha=arrancamos   #micoche.arranacar es diferente a micoche.arranacar(True)
        if self.enmarcha:
            return("el coche esta en marha")
        else:
            return("el coche esta parado")

    def estado(self):
        print("el coches tiene", self.__ruedas,"ruedas")
        print("el coche tiene un ancho",self.ancho)
        print("el coche tiene un chasis=",self.chasis)

    def chequeoInterno(self):
        print("Realizar chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            print("Todo está ok")
        else:
            print("algo está fallando")



miCoche=Coche()
print(miCoche.arrancar(True)) #SIRVE PARA ARRANCAR EL COCHE
miCoche.estado()
miCoche.chequeoInterno()

print("**********creamos el segundo objeto**************")

micoche2=Coche()
print(micoche2.arrancar(False))
micoche2.ruedas=2 #o micoche2.__rudeas=2, no afecta, yaque el valor está encapsulado
micoche2.estado()
miCoche.chequeoInterno()
