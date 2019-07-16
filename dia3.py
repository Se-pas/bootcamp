############ CONDICIONALES #############
# == igual
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que
# != distinto de
a = 10

if a > 3:
    print("Si, a es mayor a 3")

else:
    print("a no es mayor a 3")

if a == 3:
    print("a es igual a 3")

#####################
print("-----------------------")

nota = 50

if nota >= 60:
    print("PASASTE")

else:
    print("Hule")

#Ej. Crear una funcion que reciba como parametro una nota
#nota del 1 al 100 e imprima si pasaste o te aplazaste (se aprueba con 61)

def calificacion(nota):
    
    if nota >= 61:
        print("Pasaste!")
    else:
        print("Te aplazaste :(")

calificacion(50)
calificacion(60)
calificacion(61)
 
# and, or
a = 2
if a > 5 and a < 10 and a != 7: 
    print("a es mayor a 5 y menor a 10 y distinto a 7")

else:
    print("a no esta en el rango, alguna de las 3 condiciones no se cumple")

if a > 5 or a < 1:
    print("a es mayor a 5 o menor a 1")
else:
    print("a no es mayor a 5 ni menor a 1")

print(5>3) #se ejecutan las operaciones y devuelve TRUE o FALSE dependiendo de lo que pida

######################
print("-------------------------------------------")

#uso de elif "sino si"
edad = 15
if edad > 18:
    print("Deberia estar en la universidad")
elif edad > 13:
    print("deberia estar en la secundaria")
elif edad > 6:
    print("deberia estar en la primaria")
else:
    print("deberia estar en su casa")

#Anidado
edad = 15
if edad > 18:
    print("universidad")
else: 
    if edad > 13:
            print("Secundaria")
    else:
        if edad > 6:
            print("Primaria")
        else:
            print("bbdlc")

#EJERCICIO
#Crear una funcion puntaje que recibo como parametro una nota del 1 al 100 e imprima que nota sacaste
#nota < a 60 ------> 1
#nota entre 60 y 70 ------> 2
#nota entre 71 y 75 ------> 3
#nota entre 76 y 85 ------> 4
#nota mayor a 85 ------> 5

#Lista_puntajes = ["Pepe", "Marcelo", "Isco", "Zidane"]

def calificacion(puntaje):
     
    if puntaje < 60:
        print("Te aplazaste")
    elif puntaje >=60 and puntaje < 71:
        print("Pasaste con 2")
    elif puntaje >=71 and puntaje < 76:
        print("Pasaste con 3")
    elif puntaje >=76 and puntaje < 86:
        print("Pasaste con 4")
    else: 
        print("Pasaste con 5")

calificacion(49)

def tu_calificacion(puntaje):
    if puntaje < 60: 
        print("Te aplazaste")
    elif puntaje < 71:
        print("Pasaste con 2")
    elif puntaje < 76:
        print("pasaste con 3")
    elif puntaje < 86:
        print("pasaste con 4")
    else:
        print("pasaste con 5")

tu_calificacion(100)
#int convierte un string a entero 
#str convierte un entero a string

#EJERCICIO
#Pedir al usuario que ingrese tres numeros y multiplicarlos entre si, imprimir el resultado
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero:"))
num3 = int(input("Ingresa un ultimo numero:"))
print("El resultado es: ", num1*num2*num3)

#EJERCICIO 2
#Pedir al usuario un numero del 1 al 100 y llamar a la funcion que retornaba la nota que creamos
#hace un rato utilizando el valor ingresado del usuario
num1 = int(input("Ingresa un valor del 1 al 100:"))
calificacion(num1) 
#otra opcion es 
calificacion(int(input("Ingresa tu puntaje del examen")))

