class Persona: #Definicion de la clase Persona
    
    def __init__(self, un_nombre,altura,peso): #metodo constructor con argumento "un_nombre"
        #asigno la variable "mi_nombre" al argumento "un_nombre"
        self.mi_nombre = un_nombre   #el atributo es self.mi_nombre
        self.mi_altzra = altura

    def nacio(self, una_nacionalidad): #"nacio" es un metodo de la clase Persona
        #asigno la variable "nacionalidad" al argumento "una_nacionalidad"
        self.nacionalidad = una_nacionalidad 

    def saludo(self): #"saludo" es un metodo de la clase Persona que no tiene ningun argumento 
        #porque su funcion es solamente hacer print de lo las variables que ya se utilizaron en 
        #los metodos anteriores
        print("Hola, soy", self.mi_nombre, "y mi nacionalidad es", self.nacionalidad)



pepe = Persona("Pepito") #INSTANCIAR creo el objeto pepe y le asigno el valor al atributo y se asigna directamente en INIT por ser el primer elemento a ejecutarse
pepe.nacio("Inglesa") #
pepe.saludo()
print(pepe.nacionalidad)
print(pepe.mi_nombre)

