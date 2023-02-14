class Coche():
    
    def __init__(self): #estado inicial          
        self.__chasis=250
        self.__ancho = 12
        self.__ruedas=4 #la variable ruedas no sea accesible a cambios fuera de la clase
        self.__enmarcha= False
        

    def arrancar(self,arrancamos):#El seld se considera como un parametro nulo
        self.__enmarcha=arrancamos   #micoche.arranacar es diferente a micoche.arranacar(True)

        if(self.__enmarcha):
            chequeo=self.chequeoInterno()
        if(self.__enmarcha and chequeo):
            return("el coche esta en marha")
        elif(self.__enmarcha and chequeo==False):
            return("algo está mal en el chequeo")
        else:
            return("el coche esta parado")

    def estado(self):
        print("el coches tiene", self.__ruedas,"ruedas")
        print("el coche tiene un ancho",self.__ancho)
        print("el coche tiene un chasis=",self.__chasis)

    def chequeoInterno(self):
        print("Realizar chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False



miCoche=Coche()
print(miCoche.arrancar(True)) #SIRVE PARA ARRANCAR EL COCHE
miCoche.estado()

print("**********creamos el segundo objeto**************")

micoche2=Coche()
print(micoche2.arrancar(False))
micoche2.ruedas=2 #o micoche2.__rudeas=2, no afecta, yaque el valor está encapsulado
micoche2.estado()

