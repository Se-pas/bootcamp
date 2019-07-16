print(2+2)
print(3*5)
print(7/1)
#This is a comment 
print("Hello World" + " I'm at Penguin Bootcamp") #This is a concatenation

#####The next thing is a variable
a = 10
b = 45
c = a + b
print(c)

a = "Penguin "
b = "Bootcamp"
c = a + b
print(c)

a = "Penguin"
b = "Bootcamp"
print("Hi, I'm at ",a,b) #

#Ejercicio. Crear una variable nombre y una variable edad 
#con sus nombres y edades y despues imprimir: 
#Hola, me llamo____ y tengo _____ anhos

nombre = "Sebastian"
edad = 23
print("Hola, me llamo " + nombre + " y tengo " , edad , " anhos")
#Ej 2. Crear una variable hobby con tu pasatiempo 
# e imprimir
#Hola, me llamo _____ y tengo ___ anhos y mi hobby es _____
hobby = "investigar"
print("Hola, me llamo " + nombre + ", tengo " , edad , " anhos", " y mi hobby es ", hobby)

### Uso de corchetes para lista
datos = "Sebas"
alumnos = ["Jose", "Ramon", datos, "Maria"]
print(alumnos)
print(alumnos[2]) #aqui estoy llamando al alumno que se encuentra en la posicion 2 (0,1,2,3)
#y que en este caso es un elemento de una variable

### Ejercicio 3 
### Crear una lista datos que en primer lugar este tu nombre
###y en la segunda posicion este tu edad
###imprimir "Hola me llamo ____ y tengo ____ anhos"

datos1 = ["Sebastian", 23]
print("Hola me llamo",datos1[0], "y tengo", datos1[1], "anhos")

#cambiar el valor de uno de los datos, puedo llamar y simplemente
#asignarle otro valor y este nuevo valor se superpone
datos1[1] = 45
print("Hola me llamo",datos1[0], "y tengo", datos1[1], "anhos")

#agregar datos a la lista con "append"
#datos1.append("Programacion")
print(datos1)

#### Ejercicio 4
#### Agregar una profesion y un hobby a la lista datos
#### previamente creada (usar append())
#### imprimir la lista
datos1.append("CM")
datos1.append("disenhar")
print(datos1)
print("Hola me llamo",datos1[0], "y tengo", datos1[1], "anhos", "trabajo como", datos1[2], "y me gusta", datos1[3])

#Eliminar el ultimo elemento de la lista con "pop()"
datos1.pop(0)
print(datos1)

#Agregar elemento en una posicion especifica de la lista con "insert(numero de posicion, dato"
datos1.insert(2, "otro elemento")
print(datos1)

# funcion len() => lenght - "Sirve para saber la cantidad de elementos, o dimension de la lista"
print(datos1) #imprimo los datos
dimension_de_datos = len(datos1) #guardo la funcion len() en una variable (es una alternativa)
datos1.pop() #borre un dato como ejemplo
print(datos1) #imprimo los datos luego de borrar uno anterior
print(len(datos1)) #imprimo la cantidad de datos que hay (otra alternativa)

#####Ejercicio 5
#####Obtener la dimension de la lista datos e imprimir:
#####"La lista datos tiene ____ elementos"

dimension1 = len(datos1) #Creo una variable de len para luego llamarla en el print
print("La lista datos tiene", dimension1, "elementos")

#Mismo resultado sin necesidad de crear una variable
print("La lista datos tiene", len(datos1), "elementos")

######Ejercicio 6
###### Imprimir el ultimo elemento de una lista sin saber 
###### cuantos elementos tiene, pista usar len ()
###### No hacer lista_larga[27]

lista_larga = [1,2,3,4,4,4,4,5,5,6,5,5,6,8,5,7,8,45,45,45,5,5,6,7,7,8,6,5,55]
#Opcion 1
dimension2 = lista_larga[len(lista_larga)-1] #se resta -1 porque len() empieza a contar desde 1.
print(dimension2)

#Opcion 2
ultimo = len(lista_larga) -1
print(lista_larga[ultimo])

################# Bucles/Loops/Ciclos/Iteraciones #########
# Cuando se pone : (dos puntos) significa que a continuacion habra un bloque de codigo 
# que se distingue por la identacion, esta identacion es lo que lo conforma como bloque de codigo
# al quitar la identacion (no dejar espacios o tabulaciones) el bloque de codigo acaba
# y se toma como uno nuevo

lista_temas = ["variables", "listas", "tipos de datos"]

for concepto in lista_temas:
    print("Hoy aprendi", concepto)
    print("Me gusto!")
print("Luego hacemos un after")

####### Ejercicio 7 
####### Recorrer una lista e imprimir en cada ciclo el valor del elemento
####### con tres signos de admiracion
####### variables!!!

for concepto in lista_temas:
    print(concepto,"!!!")
print("FIN!!!")

# range(parametro o elemento)

for x in range(10):
    print(x)

for z in range (10):
    print("Hola",z)

######### Ejercicio 8
#Imprimir los numeros del 1 al 100 usando for y range

for y in range (1,101):
    print(y)

#Imprimir el resultado de la suma de los numeros del 1 al 100
print("----------------")


#creacion de un ACUMULADOR
suma = 0 #establecer una variable equivalente a 0 para que luego en el ciclo 0 se vaya suman
for i in range(1,11): #se crea un ciclo que crea un rango del 1 al 10
    suma = suma + i #llamo a la variable suma (0) y le digo que es igual a (0)+ el primer numero del rango
    #luego se suma y la variable suma dentro del loop queda convertido al resultado de la suma 
    # o sea suma = 1, luego 1 = 1+1 = 2, entonces suma = 2 y se vuelve a sumar con el siguiente
    # numero dentro del loop de rango ()
print(suma)