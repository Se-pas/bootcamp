#Ejercicio
#Hacer una clase que se llame vehiculo y que tenga tres atributos y uno de ellos
#sea cantidad_ruedas; y un metodo que sea definir_tipo_vehiculo que me diga
#si es "bicicleta, triciclo, auto" de acuerdo a la cantidad de ruedas.

class Vehiculo:
    cantidad_ruedas = 0
    revoluciones = 0            #Caracteristicas generales que puedo usar en cada metodo, que todos los objetos 
    peso = 0                    #lo pueden tener

    def __init__(self,ruedas, revs, weight):
        self.cantidad_ruedas = ruedas     #primero asignar una variable al parametro de la funcion que ya estableci
        self.revoluciones = revs
        self.peso = weight
        
    def definir_transporte(self):

        if self.cantidad_ruedas == 2 and self.revoluciones <= 100 and self.peso <= 10:
            print("es una bicicleta")
        else:
            print("esto no es un biciclo") 

        if self.cantidad_ruedas == 2 and self.revoluciones >= 100 and self.peso >= 200:
            print("es una moto")
            else 
        
        if self.cantidad_ruedas == 3 and self.revoluciones <= 100 and self.peso <=10:
            print("es un triciclo")

        if self.cantidad_ruedas == 4 and self.revoluciones >= 100 and self.peso >= 500:
            print("es un auto")
        
transporte = Vehiculo(4,000,9)
transporte.definir_transporte()