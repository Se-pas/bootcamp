x=0
while x != 5:
    print("Hola esto es un bucle while, se va a ejecutar siempre que x no sea igual a 5")
    x = int(input("Ingresa un numero: ")) #ingresamos un valor para x 
    print("El valor de x ahora es",x) 
print("Termino")

#Contador inverso #OBS AGREGAR INPUT
contador = 10
while contador > 0:
    print("Sigo en el bucle while")
    contador = contador - 1
    print("Te quedan", contador, "oportunidades")
print("Game over")

#Contador #AGREGAR INPUT
contador = 0
while contador < 10:
    print("Sigo en el bucle while")
    contador = contador + 1
    print("Contador ahora vale", contador)

#EJERCICIO
#Usando while pedir al usuario 5 ingredientes para hacer una pizza y agregar a una lista, 
#al final imprimir la lista
x = 5
while ingredientes > 0:
    lista = []
    ingredientes=input("Ingresa un ingrediente:")
    lista.append(ingredientes)

