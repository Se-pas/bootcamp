

#EJERCICIO
#Usando while pedir al usuario 5 ingredientes para hacer una pizza y agregar a una lista, 
#al final imprimir la lista
contador = 5
lista = [] #la lista vacia esta afuera de lo que se va a ejecutar
while contador > 0:
    ingredientes=(input("Ingresa un ingrediente:"))
    contador = contador - 1
    lista.append(ingredientes)
print("Estos son los ingredientes para una pizza:", lista)

######################
#JUEGO adivinar el numero secreto en el que me va a preguntar un numero y debo ingresar el numero correcto


numero_secreto = 7
adivino = False

while adivino == False:
    apuesta = input("Adivina el numero secreto que esta entre el 1 al 10: ")

    if int(apuesta) == numero_secreto:
        print("ACERTASTE!!!")
        adivino = True
    else:
        print("segui participando")

#EJERCICIO
#Crear un juego de adivinar el numero como el de arriba y darle pistas al usuario si el 
#numero que ingreso es mayor o menor al numero a adivinar
#pista: usar elif

numero_secreto2 = 5
adivinar = False

while adivino == False:
    bet = int(input("Adivina el numero secreto que esta entre el 1 y el 10: "))
    
    if bet == numero_secreto2:
        print("ACERTASTE!!!")
        adivino = True

    elif bet < numero_secreto2:
        print("El numero secreto es mayor a", bet)
        print("Segui probando")

    elif bet > numero_secreto2:
        print("El numero secreto es mayor que ", bet)
        print("Segui probando")

#Buscar como genera un numero aleatorio para numero_secreto
from random import randrange
print(randrange(20))

numero_secreto3 = int(randrange(20))
print(numero_secreto3)

adivinar = False

while adivino == False:
    bet = int(input("Adivina el numero secreto que esta entre el 1 y el 20: "))
    
    if bet == numero_secreto3:
        print("ACERTASTE!!!")
        adivino = True

    elif bet < numero_secreto3:
        print("El numero secreto es mayor a", bet)
        print("Segui probando")

    elif bet > numero_secreto3:
        print("El numero secreto es mayor que ", bet)
        print("Segui probando")



numero_secreto3 = int(randrange(20))
print(numero_secreto3)

adivinar = False

while adivino == False:
    bet = int(input("Adivina el numero secreto que esta entre el 1 y el 20: "))
    
    if bet == numero_secreto3:
        print("ACERTASTE!!!")
        adivino = True
    else:
        print("Segui intentando")