
class Persona: 
    edad = 0
    peso = 6766

    def __init__(self,un_nombre,una_edad):
        self.mi_nombre = un_nombre
        self.edad = una_edad
        print("Hola, naci. Me llamo:", self.mi_nombre, self.edad)

    def cumple(self):
        self.edad = self.edad + 1

pepe = Persona("Pepito", 23)  #creamos un objeto llamado Pepe del tipo PERSONA.

pepa = Persona("Pepita", 45) 


print(pepe.edad)
print(pepe.peso)
print(pepe.mi_nombre)
print(pepa.edad)

pepe.cumple()
print(pepe.edad)